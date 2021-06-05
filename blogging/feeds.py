from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post


class LatestEntriesFeed(Feed):
    title = "Coolest blog posts"
    link = "/"
    description = "Updates to my coolest blog posts"

    def items(self):
        return Post.objects.exclude(published_date__exact=None).order_by(
            "-published_date"
        )[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse("blog_detail", args=[item.pk])
