from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    def get(self, req: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    # ok
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
# Session(login)
# Forma um
# class UserSessionView(APIView):
#     def post(self, req: Request) -> Response:
#         serializer = SessionSerializer(data=req.data)
#         serializer.is_valid(raise_exception=True)
#         user = authenticate(
#             username=serializer.validated_data["username"],
#             password=serializer.validated_data["password"],
#         )
#         # ||   user = authenticate(**serializer.validated_data)
#         if not user:
#             return Response({"details": "invalid credencials"}, status=status.HTTP_404_NOT_FOUND)
#         refresh = RefreshToken.for_user(user)
#         return_dict = {
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#         }
#         return Response(return_dict, status.HTTP_200_OK)
# Forma dois
# class UserSessionView(APIView):
# def post(self, req: Request) -> Response:
#     serializer = TokenObtainPairSerializer(data=req.data)
#     serializer.is_valid(raise_exception=True)
#     return Response(serializer.validated_data, status.HTTP_200_OK)

# Melhor forma, mas foi chamado diretamente na urls.py
# class UserSessionView(TokenObtainPairView):
#     ...
