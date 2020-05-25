from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from movies.models import Movie


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, get_agreement, password=None):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            email=email,
            get_agreement=get_agreement,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, get_agreement, email, password=None):
        user = self.create_user(
            username,
            email=email,
            password=password,
            get_agreement=get_agreement,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    get_agreement = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'get_agreement']

    def __str__(self):
        return '%s' % self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Rating(models.Model):
    comment = models.TextField(blank=True, null=True)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')  # movie.ratings
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')  # user.ratings

    class Meta:
        ordering = ('-updated_at',)


# class LikeMovie(models.Model):
#     pass
