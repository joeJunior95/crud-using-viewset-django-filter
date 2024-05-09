from djano_filters.rest_framework import FilterSet

from .models import Student

class StudentFilterSet(FilterSet):
    class Meta:
        model = Student
        fields = {
            'id' : ['exact'],
            'name' : ['exact']
        }