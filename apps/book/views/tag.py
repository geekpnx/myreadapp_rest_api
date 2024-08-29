from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.book.models import Tag 
from apps.book.serializers import TagSerializer



"""
curl http://127.0.0.1:8000/api/v1/book/tag/
token_header = 'Authorization: Token 3bfab3146866a92edbbd3fcc6b33ac1546398dc3'

curl -H 'Authorization: Token 3bfab3146866a92edbbd3fcc6b33ac1546398dc3' http://127.0.0.1:8000/api/v1/book/tag/

"""
@api_view() # Define our http methods
#@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_tags(request):
    # ORM
    tags = Tag.objects.all() # Complex Data type

    # DeSerialization
    data = TagSerializer(tags, many=True) # Convert complex data type to primitive Python types

    # Return JSOn
    return Response(data.data, status=status.HTTP_200_OK)