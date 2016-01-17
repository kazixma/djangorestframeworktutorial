from django.contrib.auth.models import User

from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields=('id','username','first_name','last_name','email','password')
        read_only_fields=('username')