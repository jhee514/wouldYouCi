from rest_framework.response import Response
from django.shortcuts import HttpResponse, get_object_or_404

from .serializers import UserCreationSerializer, RatingSerializer
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
User = get_user_model()
from utils import success_collection as success, error_collection as error
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Rating


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






@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_rating_tf(request):
    user = request.user
    if Rating.objects.filter(user=user.pk).count() > 4:
        return Response(status=200, data={'rating_tf': True})
    else:
        return Response(status=200, data={'rating_tf': False})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_rating(request):
    # user = get_object_or_404(User, id=9000000)
    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(status=400, data=serializer.errors)


@api_view(['PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def patch_delete_rating(request, rating_id):
    # user_id = 9000001
    rating = get_object_or_404(Rating, id=rating_id)
    if rating.user.id == request.user.id:
        if request.method == 'PATCH':
            serializer = RatingSerializer(instance=rating, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(status=400, data=serializer.errors)

        elif request.method == 'DELETE':
            rating.delete()
            return Response(status=204)

    return Response(status=400, data={'message': '권한이 없습니다.'})
