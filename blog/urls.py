from django.urls import path
from .views import all_post, post_detail

urlpatterns = [
    path("", all_post, name="my_stories"),
    path("<int:year>/<int:month>/<int:day>/<slug:slug>/", post_detail, name="post_detail")
] 