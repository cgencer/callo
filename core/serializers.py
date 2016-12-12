from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import UserProfile

from rest_framework import serializers
from core.models import activitiesMade

class EmbedSerializer(serializers.ModelSerializer):
	class Meta:
		model = activitiesMade


class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		read_only_fields = ['created_at']
		exclude = ['user', 'is_active', 'bmi']


class UserSerializer(serializers.ModelSerializer):
	profile = UserProfileSerializer(required=False)
	password = serializers.CharField(write_only=True, required=False)

	class Meta:
		model = User
		fields = [
			'email', 'first_name', 'last_name', 'password', 'profile'
		]

	def create(self, validated_data):
		profile_data = validated_data.pop('profile')
		validated_data['username'] = validated_data.get('email', None)

		user = User.objects.create(**validated_data)
		profile = UserProfile.objects.create(user=user, **profile_data)
		return profile

	def update(self, instance, validated_data):
		profile_data = validated_data.pop('profile')

		# Update User data
		instance.username = validated_data.get('email', instance.username)
		instance.email = validated_data.get('email', instance.email)
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)

		# Update UserProfile data
		if not instance.profile:
			UserProfile.objects.create(user=instance, **profile_data)

		instance.profile.height = profile_data.get('height', instance.profile.height)
		instance.profile.weight = profile_data.get('weight', instance.profile.weight)
		instance.save()

		# Check if the password has changed
		password = validated_data.get('password', None)
		if password:
			instance.set_password(password)
			instance.save()
			update_session_auth_hash(self.context.get('request'), instance)

		return instance
