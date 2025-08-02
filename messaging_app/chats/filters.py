import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="created_at", lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name="created_at", lookup_expr='lte')
    user = django_filters.CharFilter(field_name="sender__username")

    class Meta:
        model = Message
        fields = ['user', 'start_date', 'end_date']
