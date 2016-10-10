from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..forms.comment import CommentsForm

def postview(request,postId=None):
    """
    view for full post and available comment.
    if post_id not passed redirect to page all posts.
    :param request:
    :param post_id:
    :return:
    """
    from ..models.post import Post

    if not postId: return HttpResponseRedirect('/posts/')

    article = Post.objects.get(id=postId)

    commentsForm = CommentsForm(data=request.POST)

    if request.method == 'POST':
        if commentsForm.is_valid():
            name = commentsForm.cleaned_data['name']
            comment = commentsForm.cleaned_data['message']
            _saveComment(name,comment,article)
        else:
            commentsForm = CommentsForm()

    return render(request,
                  'post/article.html',
                  {'article': article,'form': commentsForm}
                 )

def _saveComment(name,comment,postObject):
    """
    add commentary to post
    :param request:
    :return:
    """
    from ..models.comments import Comments
    comment = Comments.create(name,comment,postObject)
    comment.save()
