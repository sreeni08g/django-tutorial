from .models import Snippet
from rest_framework import serializers
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):

     #owner = serializers.ReadOnlyField(source='owner.username')

     class Meta:
        model = Snippet
        fields = ('id', 'title', 'code')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset= Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')