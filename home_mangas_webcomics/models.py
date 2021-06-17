from django.db import models

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=200, null="titre")
    link = models.CharField(max_length=200, null="lien")
    image = models.CharField(max_length=200, null="image.jpg")
    chapter = models.CharField(max_length=200, null="chapitre")
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    # def __str__(self):
    #     return '%s %s % %s' % (self.title, self.link, self.image, self.chapter, self.pub_date)