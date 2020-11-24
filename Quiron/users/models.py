""" Djanog models """
from django.db import models

""" Import the User model from django to extend """

from django.contrib.auth.models import User

class Profile(models.Model):
    """ Profile models

    Proxy model extends the base data with other information.
    """
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    prof_register = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    """ Return the user username """
    def __str__(self):
        return self.user.username