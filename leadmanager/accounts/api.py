from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
import jwt

# Register API
class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer
  permission_classes = [
    permissions.AllowAny,
  ]
  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    if user:

        payload = {
            'id': user.id,
            'email': user.email,
        }
        jwt_token = jwt.encode(payload, "SECRET_KEY")

        
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": jwt_token

    })

# Login API
class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    if user:

        payload = {
            'id': user.id,
            'email': user.email,
        }
        jwt_token = jwt.encode(payload, "SECRET_KEY")

        
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": jwt_token

    })

# Get User API
class UserAPI(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user