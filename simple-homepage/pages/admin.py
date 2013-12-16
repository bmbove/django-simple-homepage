from django.contrib import admin
from django.db import models
from django.forms import Textarea

from pages.models import Page


class PageAdmin(admin.ModelAdmin):
    model = Page
    list_display = ["id",
                    "name",
                    "active"]
    list_editable = ["active"]
    list_filter = ["active"]
    list_display_links = ["id", "name"]

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 50, 'cols': 120})}
    }

admin.site.register(Page, PageAdmin)
