from django.urls import path
from blogging.views import BlogListView, BlogDetailView
from blogging.feeds import LatestEntriesFeed

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("rss", LatestEntriesFeed()),
]
