from django.contrib import admin
from django.forms import Textarea
from django.db import models

from blog.models import Post


class BlogAdmin(admin.ModelAdmin):
    model = Post
    list_display = ["id",
                    "title",
                    "created_at",
                    "published"]
    list_editable = ["published"]
    list_filter = ["published",
                   "created_at"]
    list_display_links = ["id", "title"]

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 50, 'cols': 120})}
    }

admin.site.register(Post, BlogAdmin)
