from celery import task as app
from datetime import timedelta
from django.contrib.auth.forms import *

from django.core.mail import send_mail

from utils.models import *


@app.periodic_task(run_every=(timedelta(days=7)), name='reminder_of_us')
def hello():
    emails = []
    for user in CustomUser.objects.all():
        result = send_mail(
            'Reminder_of_us',
            'don`t forget us',
            'smtp.django@gmail.com',
            [user.email],
        )


@app.task
def send_reset_password_email(subject_template_name, email_template_name,
                              context, from_email, to_email, html_email_template_name):
    subject = loader.render_to_string(subject_template_name, context)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())
    body = loader.render_to_string(email_template_name, context)

    email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
    if html_email_template_name is not None:
        html_email = loader.render_to_string(html_email_template_name, context)
        email_message.attach_alternative(html_email, 'text/html')
    email_message.send()
