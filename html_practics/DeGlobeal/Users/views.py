from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserLoginSerializer
from django.contrib.auth import authenticate, login
from django.contrib import messages
from Users.backends import EmailBackend


# Create your views here.

class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email from the form
        password = request.POST.get('password')  # Get password from the form

        # Authenticate the user
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Invalid email or password.')  # Show error message

    return render(request, 'login.html')  # Render the login page


def home(request):
    return render(request, 'home.html')  # Render the home page