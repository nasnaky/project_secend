from rest_framework import serializers
from .models import User, FreeNoticeBoard, StoryNoticeBoard, Inquiry, Notification, suggestion_free, \
    suggestion_story, Comment_Story, Comment_ip, Comment_Free


class UserSerializers(serializers.Serializer):
    """
    user
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class FreeNoticeBoardSerializers(serializers.Serializer):
    """
    자유 게시판
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    context = serializers.CharField()
    img1 = serializers.CharField()
    img2 = serializers.CharField(allow_null=True, allow_blank=True)
    img3 = serializers.CharField(allow_null=True, allow_blank=True)
    img4 = serializers.CharField(allow_null=True, allow_blank=True)
    img5 = serializers.CharField(allow_null=True, allow_blank=True)
    create_user = serializers.IntegerField()
    create_date = serializers.DateTimeField(read_only=True)
    correction_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return FreeNoticeBoard.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.context = validated_data.get('context', instance.context)
        instance.img1 = validated_data.get('img1', instance.img1)
        instance.img2 = validated_data.get('img2', instance.img2)
        instance.img3 = validated_data.get('img3', instance.img3)
        instance.img4 = validated_data.get('img4', instance.img4)
        instance.img5 = validated_data.get('img5', instance.img5)
        instance.create_user = validated_data.get('create_user', instance.create_user)
        instance.create_date = validated_data.get('create_date', instance.create_date)
        instance.correction_date = validated_data.get('correction_date', instance.correction_date)
        instance.save()
        return instance


class StoryNoticeBoardSerializers(serializers.Serializer):
    """
    이야기
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    context = serializers.CharField()
    create_user = serializers.IntegerField()
    create_date = serializers.DateTimeField(read_only=True)
    correction_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return StoryNoticeBoard.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.context = validated_data.get('context', instance.context)
        instance.create_user = validated_data.get('create_user', instance.create_user)
        instance.create_date = validated_data.get('create_date', instance.create_date)
        instance.correction_date = validated_data.get('correction_date', instance.correction_date)
        instance.save()
        return instance


class InquirySerializers(serializers.Serializer):
    """
    문의 사항
    """

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    context = serializers.CharField()
    create_user_id = serializers.IntegerField()
    create_date = serializers.DateTimeField(read_only=True)
    correction_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Inquiry.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.context = validated_data.get('context', instance.context)
        instance.create_user_id = validated_data.get('create_user_id', instance.create_user_id)
        instance.create_date = validated_data.get('create_date', instance.create_date)
        instance.correction_date = validated_data.get('correction_date', instance.correction_date)
        instance.save()
        return instance


class NotificationSerializers(serializers.Serializer):
    """
    공지
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    context = serializers.CharField()
    img1 = serializers.ImageField()
    img2 = serializers.ImageField()
    img3 = serializers.ImageField()
    create_date = serializers.DateTimeField(read_only=True)
    correction_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Notification.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.context = validated_data.get('context', instance.context)
        instance.img1 = validated_data.get('img', instance.img1)
        instance.img2 = validated_data.get('img', instance.img2)
        instance.img3 = validated_data.get('img', instance.img3)
        instance.create_date = validated_data.get('create_date', instance.create_date)
        instance.correction_date = validated_data.get('correction_date', instance.correction_date)
        instance.save()
        return instance


class Comment_FreeSerializers(serializers.Serializer):
    """
    자유 댓글
    """
    id = serializers.IntegerField(read_only=True)
    context = serializers.CharField()
    create_id_user_fr = serializers.IntegerField()
    comment_NB = serializers.IntegerField()
    create_date = serializers.DateTimeField(read_only=True)
    correction_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Comment_Free.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.context = validated_data.get('context', instance.context)
        instance.create_id_user_fr = validated_data.get('create_id_user_fr', instance.create_id_user_fr)
        instance.comment_NB = validated_data.get('comment_NB', instance.comment_NB)
        instance.create_date = validated_data.get('create_date', instance.create_date)
        instance.correction_date = validated_data.get('correction_date', instance.correction_date)
        instance.save()
        return instance


class Comment_StorySerializers(serializers.Serializer):
    """
    스토리 댓글
    """
    id = serializers.IntegerField(read_only=True)
    context = serializers.CharField()
    create_id_user_st = serializers.IntegerField()
    comment_Story = serializers.IntegerField()
    create_date = serializers.DateTimeField(read_only=True)
    correction_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Comment_Story.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.context = validated_data.get('context', instance.context)
        instance.create_id_user_st = validated_data.get('create_id_user_st', instance.create_id_user_st)
        instance.comment_Story = validated_data.get('comment_Story', instance.comment_Story)
        instance.create_date = validated_data.get('create_date', instance.create_date)
        instance.correction_date = validated_data.get('correction_date', instance.correction_date)
        instance.save()
        return instance


class Comment_ipSerializers(serializers.Serializer):
    """
    문희 댓글
    """
    id = serializers.IntegerField(read_only=True)
    context = serializers.CharField()
    create_id_user_ip = serializers.IntegerField()
    comment_ip = serializers.IntegerField()
    create_date = serializers.DateTimeField(read_only=True)
    correction_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Comment_ip.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.context = validated_data.get('context', instance.context)
        instance.create_id_user_ip = validated_data.get('create_id_user_ip', instance.create_id_user_ip)
        instance.comment_ip = validated_data.get('comment_ip', instance.comment_ip)
        instance.create_date = validated_data.get('create_date', instance.create_date)
        instance.correction_date = validated_data.get('correction_date', instance.correction_date)
        instance.save()
        return instance


"""
추천
"""


class suggestion_storySerializers(serializers.Serializer):
    """
    스토리
    """
    id = serializers.IntegerField(read_only=True)
    user = serializers.IntegerField()
    board = serializers.IntegerField()

    def create(self, validated_data):
        return suggestion_story.objects.create(**validated_data)


class suggestion_freeSerializers(serializers.Serializer):
    """
    이미지
    """
    id = serializers.IntegerField(read_only=True)
    user = serializers.IntegerField()
    board = serializers.IntegerField()

    def create(self, validated_data):
        return suggestion_free.objects.create(**validated_data)


class UserSerializers2(serializers.ModelSerializer):
    name = UserSerializers(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        depth = 1
