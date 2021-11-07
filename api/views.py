from django.shortcuts import redirect, render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .serializers import TestSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from .models import Test
import json
from user.models import User
from django.contrib.auth.decorators import login_required

class TestView(viewsets.ModelViewSet):
    serializer_class=TestSerializer
    permission_classes= [IsAuthenticated]
    
    def get_queryset(self):
        return Test.objects.filter(user=self.request.user.id)
    
    def update(self, request, pk):
        resume=json.loads(json.dumps(request.data))['resume']
        Test.objects.filter(id=pk).update(resume=resume)
        return Response(status=status.HTTP_204_NO_CONTENT)

class OpenView(viewsets.ModelViewSet):
    serializer_class=TestSerializer
    permission_classes= [AllowAny]
    
    def get_queryset(self):
        return Test.objects.filter(user=User.objects.get(user_name=self.kwargs['name']))

def index(request):
    if request.user.is_authenticated:
     return redirect('admin:index')
    return render(request, 'api/index.html')
