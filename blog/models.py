from django.db import models
from django.template.defaultfilters import slugify


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:50] + "..."

    def pretty_date(self):
        return self.created_At.strftime('%b %m %Y')

    def save(self, *args, **kwargs):
            # Newly created object, so set slug
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
