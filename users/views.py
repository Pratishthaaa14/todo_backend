from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserDetailSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegisterView(APIView):
    permission_classes = []  # Allow any user to register

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user: User = serializer.save()   # type: ignore
            refresh = RefreshToken.for_user(user)
            return Response({
                "data": {
                    "_id": str(user.id),
                    "email": user.email,
                    "username": user.username,
                },
                "token": str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            validated = serializer.validated_data
            if not isinstance(validated, dict):
                return Response({'detail': 'Invalid login data.'}, status=status.HTTP_400_BAD_REQUEST)
            user = validated.get('user')
            access = validated.get('access')
            if user is None or access is None:
                return Response({'detail': 'Invalid login data.'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({
                "data": {
                    "_id": str(user.id),
                    "email": user.email,
                    "username": user.username,
                },
                "token": access
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class TaskListCreateView(generics.ListCreateAPIView):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'data': serializer.data})
