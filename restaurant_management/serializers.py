from django.contrib.auth.model import User
from rest_framework import serializers

class UserProfileSerilaizers(serializers.ModelSerializers):
    class Meta:
        ,odel=Userfield=["first_name","last_name","email"]