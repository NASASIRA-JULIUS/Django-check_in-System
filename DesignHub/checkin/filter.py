from django.db import models
import django_filters
from django_filters import CharFilter

from .models import visitor
 

class VisitorFilter(django_filters.FilterSet):
    Name = CharFilter(field_name='Name', lookup_expr='icontains')
    class Meta:
        model=visitor
        fields=[]
