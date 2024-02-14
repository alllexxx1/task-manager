from django.contrib.auth.models import User


class User(User):

    def __str__(self):
        return self.username
