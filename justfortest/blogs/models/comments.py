from django.db import models


class Comments(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(name="content")
    posts = models.ForeignKey('Post', related_name="posts")

    @classmethod
    def create(cls,name,content,post):
        comments = cls(
            name=name,content=content,posts=post
        )
        return comments

    class Meta:
        db_table = 'post_comment'