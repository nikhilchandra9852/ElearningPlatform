from rest_framework import serializers
from rest_framework import Users

class employeeSerializer(serializers.ModelSerializer):

	class Meta:
		model =Users
		fields= '__all__'

		
