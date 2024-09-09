from django.urls import path
from MonBlog.views import homeBlog, post_detail2, post_edit, post_delete, post_submit, infos, Accueil



urlpatterns = [
    path("homeBlog", homeBlog, name='homeBlog'),
    path('post_detail2/<int:pk>', post_detail2, name = "post_detail2"),
    path('post_submit', post_submit, name='post_submit'),
    path('post_edit/<int:pk>', post_edit, name = "post_edit"),
    path('post_delete/<int:pk>', post_delete, name = "post_delete"),
    path("infos", infos, name='infos'),
    path("Accueil", Accueil, name="Accueil")
]
