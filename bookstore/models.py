from django import forms
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
 

class Gender (models.Model):
    title: models.CharField(max_length=250)


class Author(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)

    def __str__(self) -> str:
        return self.first_name + self.last_name


class Book(models.Model):
    title = models.CharField(max_length=400)
    author = models.ManyToManyField(Author)
    pub_date = models.DateTimeField('date it was published')
    condition = models.IntegerField()
    reason_for_donation = models.CharField(max_length=400)
    photo_url = models.CharField(max_length=100)
    genders = models.ManyToManyField(Gender)


class Donor(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    rating = models.IntegerField()
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    joining_date = models.DateTimeField()
    red_flag = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name + self.last_name


class Receiver(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    rating = models.IntegerField()
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    joining_date = models.DateTimeField()
    red_flag = models.IntegerField()
    story = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.first_name + self.last_name


class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=CASCADE)
    book = models.ForeignKey(Book, on_delete=CASCADE)
    date = models.DateTimeField()
