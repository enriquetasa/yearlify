from django.db import models

from accounts.models import User
from yearlify.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from django_cryptography.fields import encrypt
import datetime

class Letter(models.Model):
    user = models.ForeignKey(User, related_name='user_letter', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now=True)
    send_on = models.DateField(null=True, blank=False)

    content = encrypt(models.TextField())

    def __str__(self):
        return "Letter by {0} created on {1}".format(self.user.email, self.created_at.strftime('%D'))

    def process(self):
        subject = "Yearlify letter for {0}".format(self.user.name)
        message = self.content 
        send_mail(subject, message, EMAIL_HOST_USER, [self.user.email], fail_silently = False)

    @classmethod
    def process_all(cls):
        for letter in cls.objects.all():
            if letter.send_on == datetime.today().date():
                letter.process()
