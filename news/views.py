from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')


def news_of_day(request):
    date = dt.date.today()
    context = {
        'date': date
    }
    return render(request, 'today_news.html', context)


def past_days_news(request, past_date):
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # raise 404 error when value error is raised/ this should redirent the user to a 404 error page
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    context = {
        'date': date
    }

    return render(request, 'past_news.html', context)


# this function will be called elsewhere to return the actual day of the week for instance in the news app
def convert_dates(dates):
    # function that gets the weekday number for the date
    day_id = dt.date.weekday(dates)

    # build a list from which each day will be retrieved
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']

    # return the actual day of the week and not just a number
    day = days[day_id]

    return day
