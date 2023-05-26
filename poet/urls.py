from django.urls import path 
import views
urlpatterns = [
    path('',views.home_page_view,name='poets'),
    path('poet=<int:poet_id>/',views.poet_books_view,name='poet books'),
    path('poet=<int:poet_id>/book=<int:cat_id>/',views.book_titles_view,name='poems titles'),
    path('poet=<int:poet_id>/book=<int:cat_id>/poem=<int:poem_id>/',views.poem_content_view, name='poem content'),
]
