
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView


# Create your views here.

class ListCreateApi(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RetrieveUpdateDestroyApi(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer