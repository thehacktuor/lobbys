from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserModel
from .serializer import UserSerializer

class AllUsers(APIView):

    def get(self, request):
        users = UserModel.objects.all()
        user_serializer = UserSerializer(users,many=True)
        return Response(user_serializer.data)

class AddUser(APIView):

    def post(self, request):

        data = {
            'name': request.data['name'],
            'age':request.data['age'],
            'type_user':request.data['type_user'],
            'mode_game':request.data['mode_game']
        }

        user = UserSerializer(data=request.data)

        if user.is_valid():
            user.save()
            return Response('User was added!')
        else:
            return Response('Did not work')

class SpecificUser(APIView):

    def get_user(self, id):
        try:
            return UserModel.objects.get(id=id)
        except UserModel.DoesNotExist:
            return Response('Doesnt exist')
    
    def get(self, request, id):
        user = self.get_user(id)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)