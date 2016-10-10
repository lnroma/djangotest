from django.shortcuts import render


def index(request):
    """
    index action for request
    :param request:
    :return:
    """
    from ..models.post import Post
    collection = Post.objects.all()
    # import pdb;pdb.set_trace()
    return render(request,'index.html',{"collection":collection})