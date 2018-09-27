from rest_framework import viewsets
from rest_framework.response import Response 
from django.core.urlresolvers import reverse
from rest_framework.permissions import (
    AllowAny,
)

class ResourceListViewSet(viewsets.ViewSet):
    """
    List of resource urls
    """

    permission_classes = [AllowAny]

    def list(self, request):
        host = request.get_host()

        urls = {
            'auth': {
                'register': host + reverse('users-api:register'),
                'login': host + reverse('users-api:login'),
                'token': host + '/api/auth/token/',
            },
            'post': {
                'list': host + reverse('posts-api:list'),
                'create': host + reverse('posts-api:create'),
                'update': host + reverse('posts-api:update', kwargs={'slug': 'post-slug'}),
                'delete': host + reverse('posts-api:delete', kwargs={'slug': 'post-slug'}),
                'detail': host + reverse('posts-api:detail', kwargs={'slug': 'post-slug'}),
            },
            'comment': {
                'list': host + reverse('comments-api:list'),
                'create': host + reverse('comments-api:create'),
                'thread': host + reverse('comments-api:thread', kwargs={'pk': 1}),
            }
        }
        
        return Response(urls)