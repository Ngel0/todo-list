from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_welcome_email(user_pk):
    user = User.objects.get(pk=user_pk)
    mail_subject = 'Welcome to ToDoList'
    message = 'Hello ' + user.username + '!! \n' + 'Welcome on Board. \n\n' + 'Organize your tasks to free your mind.'
    html_message = '<p>' + message + '</p>'
    send_mail(
        subject=mail_subject,
        message=message,
        html_message=html_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],  # todo: add email field to user registration
        fail_silently=False,
    )
    return 'Done'
