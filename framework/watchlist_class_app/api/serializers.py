from rest_framework import serializers
from ..models import Movie


# Model Serializer

class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()  # Serializer Custom field

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['id', 'name', 'description']  #Can select the fields you want to serializer
        # exclude = ['name']                      #Can exclude the fields you don't want to serialize

    def get_len_name(self, object):
        return len(object.name)

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Movie name cannot be the same as description')
        return data

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Movie name must be at least 2 characters")
        return value

# Field Serializer

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name length must be between 2 and 255 characters")
#
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Movie name cannot be the same as description')
#         return data
#
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Movie name must be at least 2 characters")
#         return value
