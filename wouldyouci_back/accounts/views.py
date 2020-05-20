from rest_framework.response import Response
from .serializers import UserCreationSerializer
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
User = get_user_model()
from utils import success_collection as success, error_collection as error
from drf_yasg.utils import swagger_auto_schema


class AccountView(APIView):

    @swagger_auto_schema(
        operation_description='회원가입',
        request_body=UserCreationSerializer,
        responses={200: success.ACCOUNTS_SUCCESS.as_md(),
                   400: error.ACCOUNTS_USERNAME.as_md() + error.ACCOUNTS_EMAIL.as_md() + error.ACCOUNTS_MULTI.as_md()}
    )
    def post(self, request):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            return Response(status=200, data={'message': success.ACCOUNTS_SUCCESS.message})

        return Response(status=400, data={'message': serializer.errors})
