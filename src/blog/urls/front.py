from  django.urls import  path
from blog.views.views import *
from rest_framework import routers
router=routers.SimpleRouter()
router.register('',BlogViewSets,basename='blog-list')
urlpatterns=[
    # path("",PostsList.as_view(), name="post_list"),
    # path("<int:pk>",PostDetails.as_view(), name="post_details")
    # path("blog/",BlogViewSets.as_view({'get':'list'}),name='BlogApi-List'),
    # path("blog/<int:pk>", BlogViewSets.as_view({'get': 'retrieve'}), name='BlogApi-Retrieve')

]+router.urls