from django.shortcuts import render

from rest_framework.views import APIView
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


class RegisterView(APIView):

    def post(self, requsest: Request) -> Response:

        serializer = RegisterSerializer(data = requsest.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            
            user_json = UserSerializer(user).data

            return Response(user_json, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
