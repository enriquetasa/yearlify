from django.db import models

from accounts.models import User

from django_cryptography.fields import encrypt

class Letter(models.Model):
    user = models.ForeignKey(User, related_name='user_letter', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now=True)
    send_on = models.DateField(null=True, blank=False)

    content = encrypt(models.TextField())

    def __str__(self):
        return "Letter by {0} created on {1}".format(self.user.email, self.created_at.strftime('%D'))

    # TODO - process method
