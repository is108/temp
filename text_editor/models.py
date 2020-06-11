from django.db import models

class Text(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

class Image(models.Model):
    image =  models.ImageField(upload_to='static/css')

class File(models.Model):
    image =  models.FileField(upload_to='static/css')
