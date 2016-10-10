from django.conf.urls import url
from ..controllers.index import index
from ..controllers.post import postview

urlpatterns = [
    url(r'^$',index,{}),
    url(r'^view/(?P<postId>\d+)/$',postview,{})
]
