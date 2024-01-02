from django.contrib import admin
from .models import Film

class FilmAdmin(admin.ModelAdmin):
    list_display = ("Userid", "password")

admin.site.register(Film, FilmAdmin)

# Register your models here.
