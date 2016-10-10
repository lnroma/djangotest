from django.db import models
from django.contrib import admin

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(name="description")
    full_text = models.TextField(name='full_text')
    tags = models.TextField(name='tags')

    @classmethod
    def create(cls, title, description, full_text, tags, comment_id):
        post = cls(
            title=title, description=description,
            tags=tags, full_text=full_text
        )
        return post

    class Meta:
        db_table = 'posts'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','description')