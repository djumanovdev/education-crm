from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from accounts.permissions import IsAdmin
from .models import Student
from .serializers import (
    StudentCreateSerializer,
    UserStudentDetailSerializer,
    StudentUpdateSerailizer,
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

            serializer = UserStudentDetailSerializer(user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        students = CustomUser.objects.filter(role="STUDENT")
        serializer = UserStudentDetailSerializer(students, many=True)
        return Response(serializer.data)


class StudentDetailView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    authentication_classes = [TokenAuthentication]

    def get_user_by_pk(self, pk: int):
        try:
            student = CustomUser.objects.filter(role="STUDENT").get(pk=pk)
            return student
        except CustomUser.DoesNotExist:
            return None

    def get(self, request: Request, pk: int) -> Response:
        student = self.get_user_by_pk(pk)
        if student:
            serializer = UserStudentDetailSerializer(student)
            return Response(serializer.data)
        else:
            return Response(
                data={"message": "user not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request: Request, pk: int) -> Response:
        student = self.get_user_by_pk(pk)
        if student:
            serializer = StudentUpdateSerailizer(
                student.student, data=request.data, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(
                data={"message": "updating error"}, status=status.HTTP_404_NOT_FOUND
            )
        else:
            return Response(
                data={"message": "user not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request: Request, pk: int) -> Response:
        student = self.get_user_by_pk(pk)
        if student:
            student.student.delete()
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                data={"message": "user not found"}, status=status.HTTP_404_NOT_FOUND
            )
