from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from API.serializer import DataSerializer
from blog.models import Post


# Create your views here.
@api_view(['GET','POST'])
def get_data(request):
    permission_classes = [IsAuthenticated]
    if request.method=='GET':
        datas=Post.objects.all()
        serializer=DataSerializer(datas,many=True)
        return JsonResponse(serializer.data,safe=False)