from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer, UserSerializer
from .models import Snippet
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Create your views here.


@api_view(['GET']) # new
def api_root(request, format=None):
    return Response({
        'users': reverse('User-list', request=request, format=format),
        'snippets': reverse('Snippet-list', request=request, format=format)
    })


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    # def list(self, request, *args, **kwargs):
    #     print(request.data)
    #     queryset = Snippet.objects.all()
    #     serializer = SnippetSerializer(data=queryset, many=True)
    #     if (serializer.is_valid()==False):
    #         return Response(status = status.HTTP_400_BAD_REQUEST)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer