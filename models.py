from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
class AboutUs(models.Model):
    content=models.TextField()

