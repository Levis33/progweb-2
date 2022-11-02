from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from logger.models import EmailTypes
from project.models import Usuario


def alert_staff(mtype, context={}):
    to = [staff.email for staff in Usuario.objects.filter(is_staff=True).all() if staff.email is not None and staff.email != '']
    send_email(to, mtype, context)


def send_email(to, mtype, context={}):
    if type(to) == str:
        to = [to]

    # context["ENVIRONMENT"] = ENVIRONMENT
    email_type = EmailTypes.objects.get(email_type=mtype)
    html_message = render_to_string('email/' + email_type.template_name + '.html', context)

    # render_to_string('email/env_container.html', context)   (html_message)

    send_mail(
        subject='[BioBD Inclusao Digital] ' + email_type.description,
        message=strip_tags(html_message),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=to,
        fail_silently=False,
        html_message=html_message
    )
