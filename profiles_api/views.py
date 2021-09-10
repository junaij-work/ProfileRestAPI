from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers
from profiles_api import models

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloApiSerializer;

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Handler for HTTP POST"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'Message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handler for HTTP PUT"""

        return Response({'Method': 'PUT'})

    def patch(self, request, pk=None):
        """Handler for HTTP PATCH"""

        return Response({'Method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handler for HTTP DELETE"""

        return Response({'Method': 'DELETE'})


class HellloViewSet(viewsets.ViewSet):
    """ViewSet class for helloworld program"""

    serializer_class = serializers.HelloApiSerializer;

    def list(self, request):
        """Returns a list of viewset features"""

        a_viewset = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Handler for HTTP POST"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'Message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handler for HTTP GET"""

        return Response({'Method': 'GET'})

    def update(self, request, pk=None):
        """Handler for HTTP PUT"""

        return Response({'Method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handler for HTTP PATCH"""

        return Response({'Method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handler for HTTP DELETE"""

        return Response({'Method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle views for profile api"""

    serializer_class = serializers.ProfileSerializer
    queryset = models.UserProfile.objects.all()
