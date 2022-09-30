from django_filters import filters
from django_filters import FilterSet

from .models import Place


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class PlaceFilter(FilterSet):

    title = filters.CharFilter(label='氏名', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('title', 'title'),
        ),
        field_labels={
            'title': '店舗名',
        },
        label='並び順'
    )

    class Meta:

        model = Place
        fields = ('title',)

