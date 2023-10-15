from django.contrib import admin
from .models import Post, Image


# Register your models here.

class ImageInline(admin.StackedInline):
    model = Image


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
admin.site.register(Post,PostAdmin)

