from django.shortcuts import get_object_or_404, render
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import UserSerializer, UserAddSerializer, TagSerializer, UsertoTagSerializer, UserCreateModelSerializer
from .models import User
from rest_framework import viewsets

# Create your views here.
class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
    # queryset = User.objects.all()

class ListUserView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.get_queryset()

class DeleteUserView(DestroyAPIView):
    serializer_class = UserSerializer
    lookup_field = 'id'
    queryset = User.objects.all()

class DetailUserView(RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'id'
    queryset = User.objects.all()

class UpdateUserView(UpdateAPIView):
    serializer_class = UserSerializer
    lookup_field = 'id'
    queryset = User.objects.all()

class CreateTag(CreateAPIView):
    serializer_class = TagSerializer

class LinkUsertoTag(UpdateAPIView):
    serializer_class = UsertoTagSerializer
    lookup_field = 'id'
    queryset = User.objects.all()

    

# Model Based View
class AddUser(CreateAPIView):
    serializer_class = UserAddSerializer
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    # else:
    #     return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class CreateUserModelViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateModelSerializer

    # def list(self, request):
    #     queryset = User.objects.all()
    #     serializer = UserCreateModelSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserCreateModelSerializer(user)
    #     return Response(serializer.data)
       
    # def create(self, request):
    #     # do your thing here
    #     return super().create(request)
    
    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)