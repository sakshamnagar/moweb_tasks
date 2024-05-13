from .models import Vendor,Store
from django.db.models.signals import post_save,m2m_changed
from django.db import transaction
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


##signal method to send email to vendors on creation

@receiver(post_save, sender=Vendor)
def send_email(sender, created, instance, **kwargs):
    if created:
        subject = f'Welcome {instance.first_name} {instance.last_name}'
        message = f'Hello {instance.first_name},\n\nWelcome! Account created!'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list)



#creating a transcation.on_commit decorator

"""def on_transaction_commit(func):
    def inner(*args, **kwargs):
        transaction.on_commit(lambda: func(*args, **kwargs))
    return inner"""


#signal method to send email to vendors if they are added in any particular store

@receiver(m2m_changed, sender=Store.vendors.through)
#@on_transaction_commit
def send_email_m2m(sender, instance, action, *args, **kwargs):
    if action == 'post_add': 
        for i in instance.vendors.all():
            subject = f'Welcome {i.first_name} {i.last_name}'
            message = f'Hello {i.first_name},\n\nYou are added to store!'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [i.email]
            send_mail(subject, message, from_email, recipient_list)
        