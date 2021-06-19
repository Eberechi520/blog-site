from django.urls import path
from .views import about_me, contact, home_page

urlpatterns = [
    path("", home_page, name="home_page"),
    path("about-me/", about_me, name="about_me"),
    path("contact-me/", contact, name="contact_me")
]