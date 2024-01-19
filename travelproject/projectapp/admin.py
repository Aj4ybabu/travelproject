from django.contrib import admin

# Register your models here.

from .models import Place, Reviews

admin.site.register(Place)
admin.site.register(Reviews)