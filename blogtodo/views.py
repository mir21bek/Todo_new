from .models import BlogModel
from .serializers import BlogSerializer, StatusBlogSerializer
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate


class BlogCreateListView(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            return BlogModel.objects.filter(user=user).order_by('-created')
        return BlogModel.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateCreateDeleteListAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return BlogModel.objects.filter(user=user)


class StatusBlogList(generics.UpdateAPIView):
    serializer_class = StatusBlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return BlogModel.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.status = not serializer.instance.status
        serializer.save()


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
        except IntegrityError:
            return JsonResponse({
                'error': 'username taken choose, another name'
            }, status=400)
    elif request.method == 'GET':
        return HttpResponse('signup page')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({"error": "please check your name or password"}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
    else:
        return HttpResponse('login page')
