from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from celery.task import periodic_task
from datetime import timedelta
@shared_task
def siusti_priminima_sodinti_is_seklu(vartotojo_el_pastas, uzklausa):
    subject = 'Priminimas sodinti iš sėklų'
    message = f'Labas! Turi atlikti šį darbą: {uzklausa}.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [vartotojo_el_pastas]

    send_mail(subject, message, from_email, recipient_list)

@periodic_task(run_every=timedelta(hours=1))
def priminti_periodiskai():
    # Čia galite sukviesti jūsų siuntimo funkciją
    pass
