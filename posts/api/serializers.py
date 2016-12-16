from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
        ]


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'content',
            'timestamp',
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'timestamp',
        ]
