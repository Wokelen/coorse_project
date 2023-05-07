from rest_framework import serializers

from ads.models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source='author.id', read_only=True)
    ad_id = serializers.IntegerField(source='ad.id', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_image = serializers.ImageField(source='author.image', read_only=True)

    class Meta:
        model = Comment
        fields = ("pk", "text", "author_id", "ad_id", "author_first_name", "author_last_name", "author_image")


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description"]


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", required=False)
    phone = serializers.CharField(source="author.phone", required=False)

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["author_id"] = request.user.pk
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context.get("request").user
        validated_data["author_id"] = user
        validated_data['ad'] = instance.ad

        return super().update(instance, validated_data)

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "phone", "description", "author_first_name", "author_last_name",
                  "author_id"]


