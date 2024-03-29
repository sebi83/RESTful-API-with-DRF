from rest_framework import serializers
from .models import Post
from users.models import UserModel


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "body", "userID")

    def create(self, validated_data):

        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.body = validated_data.get("body", instance.body)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "username")
        model = UserModel

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.userID)
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance
