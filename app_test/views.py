from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .models import Student, User
from .serializers import AnswerSerializer

# Endpoint para identificar un estudiante y devolver su JWT para registrar sus respuestas
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({'access': str(refresh.access_token)})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)

# Endpoint protegido para registrar las respuestas de un estudiante
class AnswerView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        student = Student.objects.get(user=request.user)
        user = User.objects.get(username=student.user.username)
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student=user) # Pasamos el objeto User en lugar del objeto Student
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)