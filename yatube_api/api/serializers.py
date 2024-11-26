from rest_framework import serializers
from posts.models import Post, Group, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'title', 'slug', 'description']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    group = GroupSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'text', 'pub_date', 'author', 'image', 'group']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'text', 'created']
