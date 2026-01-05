from django.contrib.auth import authenticate

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status

from .serializers import LoginSerializer


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        serilizer = LoginSerializer(data=request.data)

        if serilizer.is_valid(raise_exception=True):
            data = serilizer.validated_data
            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({"Token": token.key}, status=status.HTTP_201_CREATED)

            return Response(
                data={"message": "Bunday username yoki password mavjud emas"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        return Response(status=status.HTTP_404_NOT_FOUND)
