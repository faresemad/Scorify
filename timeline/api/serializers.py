from rest_framework import serializers

from timeline.models import Comment, Post, Story


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "slug",
            "body",
            "created_at",
            "updated_at",
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "post",
            "author",
            "body",
            "created_at",
            "updated_at",
        )


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = (
            "id",
            "author",
            "photo",
            "text",
            "created_at",
        )
