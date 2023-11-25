import time
from celery import shared_task
from stories.models import Subscriber, Recipe
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


@shared_task
def export_data():
    print("Export Start!")
    time.sleep(10)
    print("Export End!")


@shared_task
def send_mail():
    mail_list = Subscriber.objects.values_list("email", flat=True)
    recipe_list = Recipe.objects.all()[:3]
    subject = "Popular posts"
    message = render_to_string("email-subscribers.html", {"recipes": recipe_list})
    mail = EmailMultiAlternatives(
        subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=mail_list
    )
    mail.content_subtype = 'HTML'
    mail.send()
