from rest_framework.response import Response
from django.shortcuts import HttpResponse, get_object_or_404
import os
from wouldyouci_back.settings import MEDIA_ROOT
from .serializers import UserCreationSerializer, UserDetailSerializer, ProfileSerializer
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Rating, Profile


@api_view(['POST', 'PATCH'])
@permission_classes([AllowAny])
def create_user(request):
    if request.method == 'POST':
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            return Response(status=200, data={'message': '회원가입 되었습니다.'})

        return Response(status=400, data={'message': serializer.errors})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_rating_tf(request):
    user = request.user
    if Rating.objects.filter(user=user.pk).count() > 4:
        return Response(status=200, data={'rating_tf': True})
    else:
        return Response(status=200, data={'rating_tf': False})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request):
    user = get_object_or_404(User, id=request.user.id)
    serializer = UserDetailSerializer(user)

    return Response(status=200, data=serializer.data)


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def change_profile(request):
    user = request.user
    # print(request.body)
    # print(request.data)
    if Profile.objects.filter(user=user.id).exists():
        profile = Profile.objects.get(user=user.id)
        # os.remove(os.path.join(MEDIA_ROOT, f"{profile.file}"))
        profile.delete()
    if request.method == 'POST':
        if request.FILES:
            serializer = ProfileSerializer(request.POST, request.FILES)
            # print(request.data)
            if serializer.is_valid():
                profile = serializer.create(serializer.validated_data)
                profile.user_id = user.id
                profile.save()
                return Response(status=200, data={'file': f"media/{profile.file}"})
            # print(serializer.errors)
            return Response(status=400, data={'message': '유효하지 않은 파일입니다.'})
        return Response(status=403, data={'message': '이미지는 필수입니다.'})
    elif request.method == 'DELETE':
        return Response(status=204)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = get_object_or_404(User, id=request.user.id)
    # user = get_object_or_404(User, id=9000000)
    # password = request.POST.get('password')
    new_password = request.data.get('new_password')

    if not new_password:
        return Response(status=400, data={'message': '필수 데이터가 누락되었습니다.'})

    # if user.check_password(password):
    user.set_password(new_password)
    user.save()
    return Response(status=203)
    # return Response(status=403, data={'message': '비밀번호가 일치하지 않습니다.'})

