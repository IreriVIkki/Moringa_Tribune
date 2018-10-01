from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_welcome_email(name, receiver):
    # creating message subject and sender
    subject = 'Welcome to MoringaTribune Emaillist'
    sender = 'wambsviki@gmail.com'

    # passing in context variables
    text_content = render_to_string('email/email.txt', {'name': name})
    html_content = render_to_string('email/email.html', {'name': name})

    msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    pass
