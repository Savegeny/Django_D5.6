from django_filters import FilterSet, CharFilter, DateFromToRangeFilter, DateTimeFromToRangeFilter
from .models import Post


class PostFilter(FilterSet):
    date_create = DateTimeFromToRangeFilter()

    class Meta:
        model = Post
        # fields = ["date_create"]
        fields = {
            "head_post": ["icontains"],
            # "date_create": ["gte"],
            "text_post": ["icontains"],
        }
