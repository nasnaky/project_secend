from django.db import models


class User(models.Model):
    """
    사용자
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    email = models.EmailField()
    password = models.CharField(max_length=65)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.id


class FreeNoticeBoard(models.Model):
    """
    자유 개시판
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    context = models.TextField(null=True)
    img1 = models.TextField(null=True, blank=True)
    img2 = models.TextField(null=True, blank=True)
    img3 = models.TextField(null=True, blank=True)
    img4 = models.TextField(null=True, blank=True)
    img5 = models.TextField(null=True, blank=True)
    create_user = models.IntegerField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    correction_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    def __int__(self):
        return self.id


class StoryNoticeBoard(models.Model):
    """
    이야기
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    context = models.TextField()
    create_user = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    correction_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    def __int__(self):
        return self.id


class Inquiry(models.Model):
    """
    문의 사항
    """
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=100)
    context = models.TextField()
    create_user_id = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    correction_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    def __int__(self):
        return self.id


class Notification(models.Model):
    """
    공지 사항
    """
    title = models.CharField(max_length=100)
    context = models.TextField()
    img1 = models.ImageField(upload_to='image/Notification/', null=True, blank=True)
    img2 = models.ImageField(upload_to='image/Notification/', null=True, blank=True)
    img3 = models.ImageField(upload_to='image/Notification/', null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    correction_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    댓글 실험용
    """


class Comment_Free(models.Model):
    """
    프리 댓글
    """
    id = models.AutoField(primary_key=True)
    context = models.TextField()
    create_id_user_fr = models.IntegerField(null=True,blank=True)
    comment_NB = models.IntegerField(null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    correction_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.context

    def __int__(self):
        return self.id


class Comment_Story(models.Model):
    """
    스토리 댓글
    """
    id = models.AutoField(primary_key=True)
    context = models.TextField()
    create_id_user_st = models.IntegerField(null=True,blank=True)
    comment_Story = models.IntegerField(null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    correction_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.context

    def __int__(self):
        return self.id


class Comment_ip(models.Model):
    """
    문의 댓글
    """
    id = models.AutoField(primary_key=True)
    context = models.TextField()
    create_id_user_ip = models.IntegerField(null=True,blank=True)
    comment_ip = models.IntegerField(null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    correction_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.context

    def __int__(self):
        return self.id

class suggestion_story(models.Model):
    user = models.IntegerField(null=True, blank=True)
    board = models.IntegerField(null=True, blank=True)


class suggestion_free(models.Model):
    user = models.IntegerField(null=True, blank=True)
    board = models.IntegerField(null=True, blank=True)
