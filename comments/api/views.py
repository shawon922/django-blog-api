from django.db.models import Q
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.mixins import (UpdateModelMixin, DestroyModelMixin)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from comments.models import Comment

from posts.api.pagination import (
    PostLimitOffsetPagination,
    PostPageNumberPagination,
)
from posts.api.permissions import (
    IsOwnerOrReadOnly,
)
from .serializers import (
    create_comment_serializer,
    CommentSerializer,
    CommentListSerializer,
    CommentDetailSerializer,
)


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    # serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        model_type = self.request.GET.get('type')
        slug = self.request.GET.get('slug')
        parent_id = self.request.GET.get('parent_id', None)
        user = self.request.user

        return create_comment_serializer(model_type=model_type, slug=slug, parent_id=parent_id, user=user)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class CommentDetailAPIView(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
    queryset = Comment.objects.filter(id__gte=0)
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CommentListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content', 'user__username', 'user__first_name', 'user__last_name']
    serializer_class = CommentListSerializer
    pagination_class = PostPageNumberPagination # PostLimitOffsetPagination # PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        # queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Comment.objects.filter(id__gte=0)
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query)|
                Q(user__username__icontains=query)|
                Q(user__first_name__icontains=query)|
                Q(user__last_name__icontains=query)
            ).distinct()

        return queryset_list

