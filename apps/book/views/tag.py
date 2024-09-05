from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes#, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.book.models import Tag 
from apps.book.serializers import TagSerializer


"""
curl http://127.0.0.1:8000/api/v1/book/tag/
token_header='7f63777fb2fba6238acd720ac872e9cefeab36b2'

curl -H "Authorization: Token $token_header" http://127.0.0.1:8000/api/v1/book/tag/
"""
# Function-base view
@api_view(['GET'])  # By default, it uses a 'GET' method
#@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_tags(request):
    tags = Tag.objects.all()

    data = TagSerializer(tags, many=True)

    return Response(data.data, status=status.HTTP_200_OK)