from django.contrib import admin

# Register your models here.
from .models import Medicine, Name

admin.site.register(Medicine)
admin.site.register(Name)