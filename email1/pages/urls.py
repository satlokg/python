from django.urls import path
from pages.views import home, about, contact, team, member
urlpatterns = [
    path('', home),
    path('members/', team, name="team"),
    path('category/<int:cat_id>/member/<int:mem_id>', member, name="member"),
    path('about/', about),
    path('contact/', contact),
]
