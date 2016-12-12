from rest_framework import serializers

from nutrition.models import CalorieInput, CalorieOutput


class CalorieInputSerializer(serializers.ModelSerializer):
	class Meta:
		model = CalorieInput
		fields = ["date", "code", "name", "unit", "quantity", "calorie", "nutrients"]
		read_only_fields = ["id", "created_at", "updated_at"]


class CalorieOutputSerializer(serializers.ModelSerializer):
	class Meta:
		model = CalorieOutput
		fields = ["date", "code", "name", "unit", "quantity", "calorie"]
		read_only_fields = ["id", "created_at", "updated_at"]
