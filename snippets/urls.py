from .views import SnippetList
from django.urls import path

urlpatterns =[
    path('snippets',SnippetList.as_view(),  name='Snippet-list'),
    # path('snippets/<int:pk>',SnippetDetail.as_view()),
    # path('users',UserList.as_view(), name='User-list'),
    # path('users/<int:pk>',UserDetail.as_view()),
    #path('', api_root),
]