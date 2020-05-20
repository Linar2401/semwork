from datetime import datetime

from rest_framework import serializers

from books.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'book', 'user', 'text', 'pub_date')

        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'read_only': True},
            'pub_date': {'read_only': True},
        }

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        return Comment.objects.create(user=user, pub_date=datetime.now(), **validated_data)
