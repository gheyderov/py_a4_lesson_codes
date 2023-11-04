from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from drf_yasg.utils import swagger_auto_schema
from accounts.api.serializers import UserTokenSerializer

class UserTokenObtainPairView(TokenObtainPairView):

    @swagger_auto_schema(responses={200: UserTokenSerializer(many=True)})
    def post(self, request, *args, **kwargs):
        return super().post(*args, **kwargs)