from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.templatetags.static import static


class Profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
    ]

    web_choices = [('1', '1'), ('2','2'), ('3', '3'), ('4','4'), ('5', '5'), ('6','6'), ('7', '7'), ('8','8')]

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, db_index=True)
    motto = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="customers/profiles/logo/", null=True, blank=True)

    zite = models.CharField(max_length=10)
    navbar = models.CharField(max_length=20)
    stylesheet = models.CharField(max_length=20)
    
    icons = models.ManyToManyField('Icon')
    gallery = models.ManyToManyField('Gallery')
    pricing = models.ManyToManyField('Pricing')
    services = models.ManyToManyField('Services')
    testimonials = models.ManyToManyField('Testimonial')

    avatar = models.ImageField(upload_to="customers/profiles/avatars/", null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=30, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('assets/img/team/default-profile-picture.png')
    
    def __str__(self):
        return self.slug

class Services(models.Model):
    services = models.CharField(max_length=30)
    icon = models.CharField(max_length=30)

    def __str__(self):
        return self.services


class Icon(models.Model):
    icon = models.CharField(max_length=30)
    icons = models.CharField(max_length=30)
    
    fav = models.CharField(max_length=30)
    shortcut = models.CharField(max_length=30)
    

    def __str__(self):
        return self.icon


class Gallery(models.Model):
    alt_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="customers/profiles/photo/", null=True, blank=True)

    def __str__(self):
        return self.alt_name


class Testimonial(models.Model):
    person = models.CharField(max_length=30)
    quote = models.CharField(max_length=100)

    def __str__(self):
        return self.person

class Pricing(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    saving = models.CharField(max_length=20)
    payment = models.CharField(max_length=20)

    item_amount = models.IntegerField()
    item_quantity = models.CharField(max_length=10)
    item_name = models.CharField(max_length=30)

    def __str__(self):
        return self.name