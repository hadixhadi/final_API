from rest_framework import serializers
from blog.models import Post, Image

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Image
        fields = ('image_url',)
    def get_image_url(self, obj):
        domain = 'http://192.168.100.15:8000'  # Replace with your actual domain address
        if obj.image:
            return f"{domain}{obj.image.url}"
        return None

class DataSerializer(serializers.ModelSerializer):
    image_url = ImageSerializer(many=True, read_only=True)
    image=serializers.ImageField()
    class Meta:
        model = Post
        fields = ['name', 'id_code', 'father_name', 'history',
                  'life_history', 'devise','author', 'image','image_url']



class CreatePostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Post
        fields = ['name', 'id_code', 'father_name', 'history',
                  'life_history', 'devise', 'author', 'image']