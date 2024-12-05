from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def get_User(request):
    user = request.data.get('user_name', None)
    
    if user:
        try:
            user = User.objects.get(user_name=user)

            return Response({'user requested': user}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error, user not found': user}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'No username provided'}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def create_User(request):
    user_name = request.data.get('user_name')
    
    if User.objects.filter(user_name=user_name).exists():
        return Response(
            {'User already exists': user_name},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_user(request):
    user_name = request.data.get('user_name')  # Current username
    updated_name = request.data.get('updated_name')  # New username

    if user_name and updated_name:
        try:
            user = User.objects.get(user_name=user_name)
            
            if User.objects.filter(user_name=updated_name).exists():
                return Response(
                    {'error': f'User with name "{updated_name}" already exists.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            user.user_name = updated_name
            user.save()
            
            return Response(
                {'message': f'User "{user_name}" updated to "{updated_name}".'},
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {'error': f'User with name "{user_name}" not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
    else:
        return Response(
            {'error': 'Both "user_name" and "updated_name" must be provided.'},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['DELETE'])
def delete_User(request):
    user = request.data.get('user_name', None)

    if user:
        try:
            user = User.objects.get(user_name=user)
            user.delete()
            return Response({'message': f'User {user} deleted successfully'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': f'User {user} not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'No user provided'}, status=status.HTTP_400_BAD_REQUEST)