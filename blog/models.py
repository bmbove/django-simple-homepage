from django.db import models
from django.template.defaultfilters import slugify


class Post(models.Model):

    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField(max_length=255, blank=True, default='')
    published = models.BooleanField(default=False)
    content = models.TextField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
