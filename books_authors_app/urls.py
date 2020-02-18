from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('post_books', views.post_books),
	path('books/<int:id>', views.info),
	path('add_author/<int:id>', views.add_author),
	
	path('authors', views.create_author),
	path('post_authors',views.post_authors),
	path('authors/<int:id>', views.info_author),
	path('add_book/<int:id>', views.add_book),
]