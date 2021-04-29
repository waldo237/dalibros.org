from django.db import models

# Create your models here.
class Gender (models.Model):
    title: models.CharField(max_length=250)

class Book(models.Model):
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date it was published')
    condition = models.IntegerField()
    reason_for_donation = models.CharField(max_length=400)
    photo_url = models.CharField(max_length=100)
    genders = models.ManyToManyField(Gender)


class Author(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)

    def __str__(self) -> str:
        return self.first_name + self.last_name


class Donor(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    emailAddress = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return self.first_name + self.last_name


class Receiver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    emailAddress = models.EmailField(max_length=254)


class Donation(models.Model):
    donor = models.ForeignKey(Donor)
    receiver = models.ForeignKey(Receiver)
