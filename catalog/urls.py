from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^books/$', views.BookListView.as_view(), name='books'),
	url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
	url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
	url(r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
	url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
	url(r'^borrowed/$', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
]

urlpatterns += [   
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [  
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

urlpatterns += [  
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]