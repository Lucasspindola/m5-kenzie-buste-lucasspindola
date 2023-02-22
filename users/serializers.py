from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


# Desenvolva um serializador para registro de usuário.
# Esse serializador deve verificar
# também se o email e username em questão são únicos ou não. Caso não,
# deverá retornar uma mensagem adequada ao cliente.
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20, validators=[
        UniqueValidator(queryset=User.objects.all(), message="username already taken.")
    ],)
    email = serializers.CharField(max_length=127, validators=[
        UniqueValidator(queryset=User.objects.all(), message="email already registered.")
    ],)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        if_is_employee = validated_data.get('is_employee')
        if if_is_employee in (True, 1):
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)


# class SessionSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=20, write_only=True)
#     password = serializers.CharField(write_only=True)
# Não vai vir na req, mas se vier empregado, tornar isuper true e retornar duas chaves boleaan
# is_superuser = serializers.BooleanField(allow_null=True, default=False)
# # de qualquer forma deve retornar as chaves


# Você também deverá obrigatoriamente sobrescrever o método create do serializer.

# mensagem para email repetido: "email already registered."
# mensagem para username repetido: "username already taken."
