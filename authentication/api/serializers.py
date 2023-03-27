from rest_framework import serializers

from authentication import models as m


class UserSerializer(serializers.ModelSerializer):
    lookup_field = 'slug'

    class Meta:
        model = m.User
        fields = ('id', 'username', 'first_name', 'last_name', 'middle_name', 
            'email', 'gender', 'phone_number', )