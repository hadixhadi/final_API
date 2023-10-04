from django.contrib import admin
from .models import Post, Image


# Register your models here.

class ImageInline(admin.StackedInline):
    model = Image


class DataLine(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Post, DataLine)

