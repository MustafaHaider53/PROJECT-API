from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from api.pagination import MyPagination
from rest_framework.throttling import AnonRateThrottle , UserRateThrottle
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class StudentCRUD(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filter_backends = [SearchFilter]
    search_fields = ['name' , 'city' , 'roll']

    pagination_class = MyPagination

    throttle_classes = [AnonRateThrottle , UserRateThrottle]

    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]



