from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage


# def say_hello(request):
#     send_mail('subject', 'message', 'joe@gmail.com', ['joe2@gmail.com'])
#     return render(request, 'hello.html', {'name': 'Mosh'})


# def say_hello(request):
#     try:
#         mail_admins('subject', 'msg', html_message='mssg')
#     except BadHeaderError:
#         pass
#     return render(request, 'hello.html', {'name': 'Mosh'})

# def say_hello(request):
#     try:
#         message = EmailMessage('subject', 'message', 'joe@gmail.com', ['joe2@gmail.com'])
#         message.attach_file('playground/static/images/download.jpg')
#         message.send()
#     except BadHeaderError:
#         pass
#     return render(request, 'hello.html', {'name': 'Mosh'})

def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'joe'}
        )
        message.send(['joe@gmail.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
