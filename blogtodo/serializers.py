from rest_framework import serializers
from .models import BlogModel


class BlogSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    created = serializers.ReadOnlyField()

    class Meta:
        model = BlogModel
        fields = ('id', 'status', 'priority', 'title', 'description', 'created')


class StatusBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['id']
        read_only_field = ['title', 'description', 'status', 'created']
