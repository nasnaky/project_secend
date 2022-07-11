from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.db.models import Q

from .models import User, FreeNoticeBoard, StoryNoticeBoard, Inquiry, Notification, suggestion_free, \
    suggestion_story, Comment_Free, Comment_ip, Comment_Story
from .serializers import UserSerializers, FreeNoticeBoardSerializers, StoryNoticeBoardSerializers, \
    InquirySerializers, NotificationSerializers, \
    suggestion_storySerializers, suggestion_freeSerializers, \
    Comment_FreeSerializers, Comment_StorySerializers, Comment_ipSerializers

"""
    유저
"""


@api_view(["POST"])  # 회원 가입
def User_api(request):
    if request.method == "POST":
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            try:
                email_check = User.objects.get(email=email)
                return Response(status=status.HTTP_404_NOT_FOUND)
            except Exception:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])  # 회원 조회, 수정, 삭제
def User_api_pk(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = UserSerializers(user)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = UserSerializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])  # 로그인
def User_login(request):
    """
    로그인
    """
    if request.method == "POST":
        data = JSONParser().parse(request)
        search_email = data['email']
        try:
            same_email = User.objects.get(email=search_email)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if data['password'] == same_email.password:
            serializer = UserSerializers(same_email)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


"""
    공지 사항
"""


@api_view(["GET"])  # 목록 출력
def Notification_api_list(request):
    if request.method == "GET":
        ApiList = Notification.objects.order_by('-create_date')
        serializer = NotificationSerializers(ApiList, many=True)
        return Response(serializer.data)


@api_view(["GET"])  # 조회
def Notification_api(request, pk):
    try:
        notification = Notification.objects.get(pk=pk)
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = NotificationSerializers(notification)
        return Response(serializer.data)


"""
    문의 사항
"""


@api_view(["GET"])  # 목록 출력
def Inquiry_api_list(request):
    if request.method == "GET":
        ApiList = Inquiry.objects.order_by('-create_date')
        serializer = InquirySerializers(ApiList, many=True)
        return Response(serializer.data)


@api_view(["POST"])  # 제작
def Inquiry_api_craete(request):
    if request.method == "POST":
        serializer = InquirySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def Inquiry_api_detail(request, pk):
    try:
        inquiry = Inquiry.objects.get(pk=pk)
    except Inquiry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = InquirySerializers(inquiry)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = InquirySerializers(inquiry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        inquiry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
    추천 
"""


@api_view(["POST"])  # 이야기
def suggestionStory_create(request):
    if request.method == "POST":
        serializer = suggestion_storySerializers(data=request.data)
        if serializer.is_valid():
            try:
                user_id = serializer.validated_data.get('user')
                board_id = serializer.validated_data.get('board')
                ss = suggestion_story.objects.get(Q(user=user_id) and Q(board=board_id))
                ss.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Exception:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])  # 이야기 수
def suggestionStory_count(request, pk):
    if request.method == "GET":
        data = suggestion_story.objects.filter(board=pk)
        serializer = len(data)
        return Response(serializer)


@api_view(["POST"])  # 자유
def suggestionFree_create(request):
    if request.method == "POST":
        serializer = suggestion_freeSerializers(data=request.data)
        if serializer.is_valid():
            try:
                user_id = serializer.validated_data.get('user')
                board_id = serializer.validated_data.get('board')
                ss = suggestion_free.objects.get(Q(user=user_id) and Q(board=board_id))
                ss.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Exception:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])  # 자유 수
def suggestionFree_count(request, pk):
    if request.method == "GET":
        data = suggestion_free.objects.filter(board=pk)
        serializer = len(data)
        return Response(serializer)


"""
    스토리
"""


@api_view(["GET"])  # 리스트
def StoryNoticeBoard_api_list(request):
    if request.method == "GET":
        StoryNBList = StoryNoticeBoard.objects.order_by('-create_date')
        serializer = StoryNoticeBoardSerializers(StoryNBList, many=True)
        return Response(serializer.data)


@api_view(["POST"])
def StoryNoticeBoard_api_Create(request):
    if request.method == "POST":
        serializer = StoryNoticeBoardSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def StoryNoticeBoard_api_detail(request, pk):
    try:
        StoryNB = StoryNoticeBoard.objects.get(pk=pk)
    except StoryNoticeBoard.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = StoryNoticeBoardSerializers(StoryNB)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = StoryNoticeBoardSerializers(StoryNB, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        StoryNB.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
    자유
"""


@api_view(["GET"])
def FreeNB_api_list(request):
    if request.method == "GET":
        FreeNB = FreeNoticeBoard.objects.order_by('-create_date')
        serializer = FreeNoticeBoardSerializers(FreeNB, many=True)
        return Response(serializer.data)


@api_view(["POST"])
def FreeNB_api_create(request):
    if request.method == "POST":
        serializer = FreeNoticeBoardSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def FreeNB_api_detail(request, pk):
    try:
        FreeNB = FreeNoticeBoard.objects.get(pk=pk)
    except FreeNoticeBoard.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = FreeNoticeBoardSerializers(FreeNB)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = FreeNoticeBoardSerializers(FreeNB, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        FreeNB.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
    댓글
"""


# 프리
@api_view(["GET"])
def Comment_Free_api_list(request, pk):
    if request.method == "GET":
        try:
            comment = Comment_Free.objects.filter(comment_NB=pk)
            serializer = Comment_FreeSerializers(comment, many=True)
            return Response(serializer.data)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def Comment_Free_api_create(request):
    if request.method == "POST":
        serializer = Comment_FreeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "DELETE"])
def Comment_Free_api_detail(request, pk):
    try:
        FreeNB = Comment_Free.objects.get(pk=pk)
    except Comment_Free.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = Comment_FreeSerializers(FreeNB, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        FreeNB.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 스토리
@api_view(["GET"])
def Comment_Story_api_list(request, pk):
    if request.method == "GET":
        try:
            comment = Comment_Story.objects.filter(comment_Story=pk)
            serializer = Comment_StorySerializers(comment, many=True)
            return Response(serializer.data)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def Comment_Story_api_create(request):
    if request.method == "POST":
        serializer = Comment_StorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "DELETE"])
def Comment_Story_api_detail(request, pk):
    try:
        StoryNB = Comment_Story.objects.get(pk=pk)
    except Comment_Story.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = Comment_StorySerializers(StoryNB, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        StoryNB.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 문의 사항
@api_view(["GET"])
def Comment_ip_api_list(request, pk):
    if request.method == "GET":
        try:
            comment = Comment_ip.objects.filter(comment_ip=pk)
            serializer = Comment_ipSerializers(comment, many=True)
            return Response(serializer.data)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
