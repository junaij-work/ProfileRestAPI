from rest_framework import serializers

class HelloApiSerializer(serializers.Serializer):
    """Serializer for HelloAPI"""

    name = serializers.CharField(max_length=10)
    
