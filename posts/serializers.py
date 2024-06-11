from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from category.models import Category


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    category_name = serializers.ReadOnlyField(source='category.name')

    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name',
        allow_null=True,
        required=False
    )

    def validate_image(self, value):
        """
        Validates the image size and dimensions.

        Raises:
            serializers.ValidationError:
            If image size or dimensions exceed the limits.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        """
        Determines if the current user
        is the owner of the post.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Retrieves the ID of the like
        associated with the post, if any.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_category_name(self, obj):
        """
        Retrieves the name of the category
        associated with the post, if any.
        """
        return obj.category.name if obj.category else None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter',
            'like_id', 'likes_count', 'comments_count',
            'category', 'category_name',
        ]
