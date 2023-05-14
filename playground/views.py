from django.shortcuts import render
# from django.core.cache import cache
from django.views.decorators.cache import cache_page
import requests
from rest_framework.views import APIView
from django.utils.decorators import method_decorator


# from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
# from templated_mail.mail import BaseEmailMessage


class HelloView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        return render(request, 'hello.html', {'name': "joe"})


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

# def say_hello(request):
#     try:
#         message = BaseEmailMessage(
#             template_name='emails/hello.html',
#             context={'name': 'joe'}
#         )
#         message.send(['joe@gmail.com'])
#     except BadHeaderError:
#         pass
#     return render(request, 'hello.html', {'name': 'Mosh'})

# def say_hello(request):
#     key = 'httpbin_result'
#     if cache.get(key) is None:
#         response = requests.get('https://httpbin.org/delay/2')
#         data = response.json()
#         cache.set(key, data)
#     return render(request, 'hello.html',{'name': cache.get(key)})
#
# @cache_page(5 * 60)
# def say_hello(request):
#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()
#     return render(request, 'hello.html', {'name': data})
