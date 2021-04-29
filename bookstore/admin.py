from django.contrib import admin

# Register your models here.
from .models import Donation, Book, Author, Donor, Receiver, Gender

admin.site.site_header = "dalibrosAdmin"
admin.site.site_title = "Bienvenidos a da libros Admin"
admin.site.register(Donation)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Donor)
admin.site.register(Receiver)
admin.site.register(Gender)
