from rest_framework import serializers
from account.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style = {"input_type":"password"},write_only = True)

     
    class Meta:
        model = User
        fields = ["email","name","password",'password2',"tc"]
        extra_kwargs = {"password":{"write_only":True}} 
        # extra_kwargs = {"password":{"write_only":True},"password2":{"write_only":True}}
         
    def validate(self,attrs):
        password = attrs["password"]
        password2 = attrs["password2"]
        if password != password2:
            raise serializers.ValidationError("Passwords must match")
        return attrs
    
    def create(self,validated_data):
        return User.objects.create_user(**validated_data) 
    
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email","password"]
        
        
        

    