from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class Adv(models.Model):
    date = models.DateField()
    type = models.IntegerField()
    price = models.IntegerField()

    user = models.ForeignKey('User')
    obj = models.ManyToManyField('Object')

class Object(models.Model):

    key_feature = models.CharField(max_length=20L)
    value_feature = models.CharField(max_length=20L)

    def __unicode__(self):
        return "adv(%s) %s:%s" % (str(self.adv.id), self.key_feature, self.value_feature)


class VCard(models.Model):
    """
        Represents a virtual card (desired offers)
    """
    vcard_name = models.CharField(max_length=20L)
    date = models.DateField()

    user = models.ForeignKey('User')
    requirements =  models.ManyToManyField('VCardRequirement')

class VCardRequirement(models.Model):
    """
        Represent features of a virtual card.
    """

    key_feature = models.CharField(max_length=20L)
    value_feature = models.CharField(max_length=20L)

    # vcard = models.OneToOneField(VCard)

    def __unicode__(self):
        return "%s:%s" % (self.key_feature, self.value_feature)




class Message(models.Model):
    """
        Represents a message sent from a reader to an adv
        owner.
            - adv : The adv in subject.
            - user_ins: The owner of the adv and recipient of the message.
            - user_read: The user interested in the adv and sender of the message.
    """
    adv = models.ForeignKey(Adv)
    user_ins = models.ForeignKey('User', related_name='recipient')
    user_read = models.ForeignKey('User', related_name='sender')
    date = models.DateField()
    message = models.TextField()

    def __unicode__(self):
        return "From: %s to: %s subject: %s" % \
                    (self.user_read.username, self.user_ins.username, self.adv.id)



class FriendList(models.Model):
    id_friend = models.IntegerField()
    id_user = models.IntegerField()
    key_feature = models.CharField(max_length=20L)
    value_feature = models.CharField(max_length=20L)
    social = models.CharField(max_length=15L)


    class Meta:
        unique_together = ("id_friend", "social")

class CustomUserManager(BaseUserManager):
    """
        Custom Manager for the User model.
        Defines create_user and create_superuser.
    """
    
    def create_user(self, username, first_name, last_name, email, password):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """

        now = timezone.now()
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            email=CustomUserManager.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            registration_date=now
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username, date of
        birth and password.
        """
        user = self.create_user(username,
            password=password,
            
            )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
        Inherits from AbstractBaseUser to define a custom 
        user model for authentication instead of Django's 
        default user model. (django.contrib.auth.models.User)
    """
    username = models.CharField(unique=True, max_length=20L)
    email = models.CharField(max_length=40L)
    first_name = models.CharField(max_length=20L)
    last_name = models.CharField(max_length=20L)
    photo = models.CharField(max_length=50L)
    city = models.CharField(max_length=20L)
    phone = models.CharField(max_length=15L)
    registration_date = models.DateTimeField()

    objects = CustomUserManager()

    USERNAME_FIELD = 'username' # Identifies the user during authentication.
    REQUIRED_FIELD = ['first_name', 'last_name', 'email', 'password']



