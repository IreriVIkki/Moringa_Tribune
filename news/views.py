from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Article, NewsLetterRecipients
import datetime as dt
from .forms import NewsLetterForm
from .email import send_welcome_email


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')


def news_of_day(request):
    date = dt.date.today()
    news = Article.todays_news()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)
            HttpResponse('news_of_day')
    else:
        form = NewsLetterForm()
    context = {
        'date': date,
        'news': news,
        'letterform': form
    }
    return render(request, 'today_news.html', context)


def past_days_news(request, past_date):
    try:
        # converts data from the passed date string to a date time object
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # raise 404 error when value error is raised/ this should redirent the user to a 404 error page
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    news = Article.days_news(date)

    context = {
        'date': date,
        'news': news
    }

    return render(request, 'past_news.html', context)


def search_results(request):
    if 'article' in request.GET and request.GET['article']:
        search_term = request.GET.get('article')
        searched_articles = Article.search_by_title(search_term)
        message = f'{search_term}'

    else:
        message = 'You havent searched any article'

    return render(request, 'search.html', {
        'articles': searched_articles,
        'message': message
    })


def article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        raise Http404
    context = {
        'article': article
    }
    return render(request, 'article.html', context)
