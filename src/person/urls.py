from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorList, BookList, AuthList, AuthorRetrieve

router = DefaultRouter()
router.register(r'books', BookList)

urlpatterns = [
    path('', include(router.urls)),
    path('authe/', AuthList.as_view(), name='Token'),
    path(r'authors/', AuthorList.as_view()),
    path(r'authors/<int:pk>/', AuthorRetrieve.as_view()),
]