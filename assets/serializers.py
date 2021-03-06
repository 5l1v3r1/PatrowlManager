# -*- coding: utf-8 -*-

from rest_framework import serializers, generics
from common.utils.pagination import StandardResultsSetPagination
from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters
from django_filters import FilterSet, OrderingFilter
from .models import Asset


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ('id', 'value', 'name', 'type', 'owner', 'description',
            'criticity', 'status', 'created_at', 'updated_at')


class AssetFilter(FilterSet):
    sorted_by = OrderingFilter(
        # tuple-mapping retains order
        choices=(
            ('value', _('Value')),
            ('-value', _('Value (desc)')),
            ('name', _('Name')),
            ('-name', _('Name (desc)')),
            ('criticity', _('Criticity')),
            ('-criticity', _('Criticity (desc)')),
            ('type', _('Type')),
            ('-type', _('Type (desc)')),
        )
    )

    class Meta:
        model = Asset
        fields = {
            'name': ['icontains'],
            'value': ['icontains'],
            'description': ['icontains'],
        }


class AssetList(generics.ListAPIView):
    serializer_class = AssetSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AssetFilter
    filterset_fields = ('id', 'name', 'value', 'criticity', 'type')
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Asset.objects.all().order_by('value')
