from django.urls import path
from blogging.views import PostListView, PostDetailView, LatestBlogUpdates

urlpatterns = [
    # path('', list_view, name="blog_index"),
    path("", PostListView.as_view(), name="post_index"),
    path(
        "posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"
    ),  # <int:post_id> captures digits as the post_id
    path('latest/feed/', LatestBlogUpdates()),
]
