from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_At = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

    def pretty_date(self):
        return self.created_At.strftime('%b %m %Y')
