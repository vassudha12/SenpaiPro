from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_by_id, name='book_by_id'),
    # path('book/<int:book_id>',views.book_by_id,name='book_by_id'),
]
