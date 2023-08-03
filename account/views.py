from rest_framework.response import Response

from rest_framework import status
from rest_framework.views import APIView

from account.serializers import UserLoginSerializer
from django.contrib.auth import authenticate


from account.serializers import UserRegistrationSerializer
from account.serializers import UserLoginSerializer

# class UserRegistrationView(APIView):
#     def get(self,request,format = None):
#         return Response({"message":"User registration view sucess"},status = status.HTTP_200_OK)

class UserRegistrationView(APIView):
    def post(self,request,format = None):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            user = serializer.save()
            return Response({"message":"User registration view sucess"},status = status.HTTP_200_OK)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST) 

              
        

        # return Response({"message":"User registration view sucess"},status = status.HTTP_200_OK)

class UserLoginView(APIView):
    def post(self,request,format = None):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            # authenticate(email = email,password = password)
            user =authenticate(email = email,password = password)
            if user is not None:
                return Response({"message":"User login view sucess"},status = status.HTTP_200_OK)
            else:
                return Response({"message":"User login view failed"},status = status.HTTP_400_BAD_REQUEST)                  
        return Response({"message":"User login view sucess"},status = status.HTTP_200_OK)   