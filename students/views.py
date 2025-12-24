from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import RetrieveAPIView

from accounts.permissions import IsAdmin
from .models import Student
from .serializers import StudentCreateSerializer, StudentRetrieveSerializer

CustomUser = get_user_model()


class StudentsView(APIView):
    #permission_classes = [IsAdmin]
    #authentication_classes = [TokenAuthentication]

    def post(self, request: Request) -> Response:
        serializer = StudentCreateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data

            existing_user = CustomUser.objects.filter(
                username=validated_data["username"]
            ).first()
            if existing_user:
                return Response(
                    {"message": "username allaqachon band"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            existing_student = Student.objects.filter(
                phone_number=validated_data["phone_number"]
            ).first()
            if existing_student:
                return Response(
                    {"message": "phone number allaqachon band"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user = CustomUser(username=validated_data["username"])
            user.set_password(validated_data["password"])
            user.save()

            student = Student(
                account=user,
                full_name=validated_data["full_name"],
                phone_number=validated_data["phone_number"],
            )
            student.save()

            serializer = {
                "username": student.account.username,
                "full_name": student.full_name,
                "phone_number": student.phone_number,
                "role": student.account.role,
                "is_risk": student.is_risk,
                "status": student.status,
            }

            return Response(serializer, status=status.HTTP_201_CREATED)

class StudentsRetrieveView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentRetrieveSerializer