"""SemWork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from books.views import *

app_name = 'books'

urlpatterns = [
    path('book/view/<int:pk>', BookView.as_view(), name="view"),
    path('book/create/', BookCreateView.as_view(), name="create"),
    path('book/create/<int:request_id>', BookCreateByRequestView.as_view(), name="create_by_request"),
    path('book/update/<int:pk>', BookUpdateView.as_view(), name="update"),
    path('book/delete/<int:pk>', BookDeleteView.as_view(), name="delete"),
    path('book/list/<int:author_id>', BookListByAuthorView.as_view(), name='list'),
    path('book/list/request/<int:request_id>', BookListByRequestView.as_view(), name='list_by_request'),
    path('review/view/<int:pk>', ReviewView.as_view(), name="review_view"),
    path('review/create/<int:book_id>', ReviewCreateView.as_view(), name="review_create"),
    path('review/update/<int:pk>', ReviewUpdateView.as_view(), name="review_update"),
    path('review/delete/<int:pk>', ReviewDeleteView.as_view(), name="review_delete"),
    path('review/list/<int:author_id>', ReviewListByAuthorView.as_view(), name='review_list'),
    path('review/list/book/<int:id>', ReviewListByBookView.as_view(), name='review_list_by_book'),
    path('request/create/', BookRequestCreateView.as_view(), name="request_create"),
    path('request/update/<int:pk>', BookRequestUpdateView.as_view(), name="request_update"),
    path('request/delete/<int:pk>', BookRequestDeleteView.as_view(), name="request_delete"),
    path('request/list/<int:author_id>', RequestListByAuthorView.as_view(), name='request_list'),
    path('request/view/<int:pk>', BookRequestView.as_view(), name="request_view"),
    path('collection/create/', BookCollectionCreateView.as_view(), name="collection_create"),
    path('collection/update/<int:pk>', BookCollectionUpdateView.as_view(), name="collection_update"),
    path('collection/delete/<int:pk>', BookCollectionDeleteView.as_view(), name="collection_delete"),
    path('collection/list/<int:author_id>', CollectionListByAuthorView.as_view(), name='collection_list'),
    path('collection/view/<int:pk>', CollectionView.as_view(), name="collection_view"),
    path('comment/create/<int:pk>', CommentCreateView.as_view(), name="comment_create"),
    path('all/books', AllBooks.as_view(), name="books"),
    path('all/reviews', AllReviews.as_view(), name="reviews"),
    path('all/collections', AllCollections.as_view(), name="collections"),
    path('all/requests', AllRequest.as_view(), name="requests"),
]