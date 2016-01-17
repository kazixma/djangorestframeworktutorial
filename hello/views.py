from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import UserSerializer


class Usuario(APIView):
    serializer_class = UserSerializer

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id=None, format=None):

        snippet = self.get_object(id)
        serializer = UserSerializer(snippet)
        return Response(serializer.data)
        # if id != None:
        #     users = get_object_or_404(User, pk=id)
        #     many = False
        #     print('hello')
        # else:
        #     users = User.objects.all()
        #     many = True
        #     print('hello2')
        # response = self.serializer_class(users, many=many)
        #
        # return Response({'result': response.data})

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = User.objects.get(id=id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id, format=None):
        snippet = self.get_object(id=id)
        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




usuarios = Usuario.as_view()
