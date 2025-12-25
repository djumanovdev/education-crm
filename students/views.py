from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from accounts.permissions import IsAdmin
from .models import Student
from .serializers import (
    StudentCreateSerializer,
    StudentListserializer,
    StudentGetOneSerializer,
    StudentUpdateSerializer,
)

CustomUser = get_user_model()


class StudentsView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    authentication_classes = [TokenAuthentication]

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


class StudentDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    authentication_classes = [TokenAuthentication]

    def delete(self, request: Request, student_id: int) -> Response:
        student = Student.objects.filter(id=student_id).first()
        if not student:
            return Response(
                {"message": "Student topilmadi"},
                status=status.HTTP_404_NOT_FOUND,
            )

        student.account.delete()
        student.delete()

        return Response(
            {"message": "Student muvaffaqiyatli o'chirildi"},
            status=status.HTTP_200_OK,
        )

    def get(self, request: Request, student_id: int) -> Request:
        try:
            student = Student.objects.get(id=student_id)

        except Student.DoesNotExist:
            return Response(
                {"message": "Student Topilmadi"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = StudentGetOneSerializer(student)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentsListView(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    authentication_classes = [TokenAuthentication]
    queryset = Student.objects.all()
    serializer_class = StudentListserializer


class StudentUpdateView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    authentication_classes = [TokenAuthentication]
    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer
    lookup_field = "id"
