from rest_framework import serializers
from blog.models import Post, Image

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ('image_url',)

    def get_image_url(self, obj):
        domain = 'http://127.0.0.1:8000'  # Replace with your actual domain address
        if obj.image:
            return f"{domain}{obj.image.url}"
        return None

class DataSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['name', 'id_code', 'father_name', 'history', 'life_history', 'devise', 'image']
