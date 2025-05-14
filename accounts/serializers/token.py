from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username  # dans le payload JWT
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username  # dans la réponse JSON
        return data
