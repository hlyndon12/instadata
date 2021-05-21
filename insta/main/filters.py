import django_filters
from .models import UserModel,Cities
from distutils.util import strtobool


class FollowerFilter(django_filters.FilterSet):
    follower_count__gt = django_filters.NumberFilter(
        field_name='follower_count', lookup_expr='gte')
    follower_count__lt = django_filters.NumberFilter(
        field_name='follower_count', lookup_expr='lte')
    following_count__gt = django_filters.NumberFilter(
        field_name='following_count', lookup_expr='gte')
    following_count__lt = django_filters.NumberFilter(
        field_name='following_count', lookup_expr='lte')
    # city = django_filters.TypedMultipleChoiceFilter(
    #     field_name='city', choices = tuple(CHOICE),coerce=strtobool
    # )
    class Meta:
        model = UserModel
        fields = ['city','category']
