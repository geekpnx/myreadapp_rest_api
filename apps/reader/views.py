from apps.reader.models import Reader
from apps.reader.serializer import ReaderSerializer

from django.contrib.auth import authenticate # Help in authenticating the user agains username and password
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

class Login(APIView):

    def post(self, request):
        # Extract credentials
        password = request.data.get('password')
        username = request.data.get('username')

        # Authenticate the user
        user: User | None = authenticate(
            username=username,
            password=password
        )

        # Generate Token
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'data': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Invalid_Credential', 'detail': 'Username or password is incorrect'}, status=status.HTTP_404_NOT_FOUND)
        
#api/v1/reader/1
@api_view()
def detail_reader(request, pk):
    # Get Reader by pk

    reader = Reader.objects.get(user_id=pk) # Native Python Data type 

    data = ReaderSerializer(reader) 

    return Response({'data':data.data})


