from django.db import models
from django.template.defaultfilters import slugify


class Page(models.Model):

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)
    content = models.TextField()
    active = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, blank=True, default='')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Page, self).save(*args, **kwargs)
