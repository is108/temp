from django.contrib import admin

from .models import Text, Image, File

admin.site.register(Text)
admin.site.register(Image)
admin.site.register(File)
