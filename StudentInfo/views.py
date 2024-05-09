from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Student 
from .serializers import StudentSerializer 


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['name']
    search_fields =['name','id']
    ordering_fields = ['name','id']