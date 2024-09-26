from zipapp import create_archive

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, AuthUser
from rest_framework_simplejwt.tokens import Token

from vehicle.models import Car, Moto, Milage
from vehicle.validators import TitleValidator
import re


class MilageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milage
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    last_milage = serializers.IntegerField(source='milage.all.first.milage')
    milage = MilageSerializer(many=True)

    class Meta:
        model = Car
        fields = '__all__'


class MotoSerializer(serializers.ModelSerializer):
    last_milage = serializers.SerializerMethodField()

    @staticmethod
    def get_last_milage(obj):
        if obj.milage.all().first():
            print(obj.milage)
            return obj.milage.all().first().milage
        return 0

    class Meta:
        model = Moto
        fields = '__all__'


class MotoMilageSerializer(serializers.ModelSerializer):
    moto = MotoSerializer()
    class Meta:
        model = Milage
        fields = ['milage', 'year', 'moto', ]

class MotoCreateSerializer(serializers.ModelSerializer):
    milage = MilageSerializer(many=True)
    class Meta:
        model = Moto
        fields = '__all__'
        validators = [TitleValidator(field='title'), serializers.UniqueTogetherValidator(queryset=Moto.objects.all(),
                                                                                         fields=['title', 'description'])]

    def create(self, validated_data):
        milage = validated_data.pop('milage')
        moto_item = Moto.objects.create(**validated_data)
        for m in milage:
            Milage.objects.create(moto=moto_item, **m)

        return moto_item


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user: AuthUser) -> Token:
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token
