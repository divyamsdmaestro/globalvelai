from django.db.models import fields
from rest_framework import serializers

from .models import User
from .models import Tag


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = (
#             'first_name', 'email_address')

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    email_address = serializers.EmailField()
    tag_id = serializers.IntegerField()
    # is_active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        # u = User(**validated_data)
        # u.save()
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data["first_name"]
        instance.email_address = validated_data["email_address"]
        instance.save()
        return instance


    # def delete(self, validated_data):
    #     return User.objects.delete(**validated_data)

    # def update(self, validated_data):
    #     return User.objects.update(**validated_data)


    # def save(self):
    #     first_name = self.validated_data['first_name']
    #     email_address = self.validated_data['email_address']

class UserAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name']

class TagSerializer(serializers.Serializer):
    tag_name = serializers.CharField(max_length=30)
    id = serializers.IntegerField()

    def create(self, validated_data):
        return Tag.objects.create(**validated_data)


# class UsertoTagUpdatrSerializer(serializers.ModelSerializer):


#     # tag = TagSerializer()
#     # tag_id  =  serializers.IntegerField()
#     tag_id = serializers.PrimaryKeyRelatedField()

#     def update(self, instance, validated_data):
#         # instance.first_name = validated_data["first_name"]
#         # instance.email_address = validated_data["email_address"]
#         if validated_data["tag_id"]:
#             TagId = validated_data["tag_id"]
#             find_tag = Tag.objects.filter(id=TagId)
#             if find_tag:
#                 instance.tag = find_tag.id
#                 instance.save()
#         return instance



class UsertoTagSerializer(serializers.Serializer):
    # tag = TagSerializer()
    # tag_id  =  serializers.IntegerField()
    tag = serializers.IntegerField()

    def update(self, instance, validated_data):
        # instance.first_name = validated_data["first_name"]
        # instance.email_address = validated_data["email_address"]
        # print(instance.id)
        # breakpoint()
        instance.tag = validated_data["tag"]
        find_tag = Tag.objects.get(id=instance.tag)
        # print(find_tag.id)
        # breakpoint()
        # serializers = TagSerializer(find_tag, many=True)
        # print(serializers.data)
        # breakpoint()
        # instance = User.objects.get(id=instance.id)
        instance.tag = find_tag.id
        instance.save()
        # print(instance)
        # breakpoint()
        return instance

    # is_active = serializers.BooleanField(default=True)

    # def create(self, validated_data):
    #     # u = User(**validated_data)
    #     # u.save()
    #     tag_id = Tag.objects.filter(id=validated_data["tag_id"])
    #     if tag_id:
    #         return User.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.tag = validated_data["tag"]
    #     if instance.tag:
    #         Tag.objects.filter(id=instance.tag)
    #         instance.save()
    #     return instance

class UserCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = '__all__'