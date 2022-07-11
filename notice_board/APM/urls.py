from django.urls import path

from .views import User_api, User_api_pk, User_login, \
    Notification_api_list, Notification_api, \
    Inquiry_api_list, Inquiry_api_detail, Inquiry_api_craete, \
    suggestionStory_create, suggestionStory_count, suggestionFree_create, suggestionFree_count \
    , StoryNoticeBoard_api_list, StoryNoticeBoard_api_Create, StoryNoticeBoard_api_detail \
    , FreeNB_api_list, FreeNB_api_create, FreeNB_api_detail, \
    Comment_Free_api_list, Comment_Free_api_create, Comment_Free_api_detail, \
    Comment_Story_api_list, Comment_Story_api_create, Comment_Story_api_detail, \
    Comment_ip_api_list

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('User/', User_api),
    path('login/', User_login),
    path('User/<int:pk>', User_api_pk),

    path('Noti/', Notification_api_list),
    path('Noti/<int:pk>', Notification_api),

    path('Inq/', Inquiry_api_list),
    path('Inq/CRE/', Inquiry_api_craete),
    path('Inq/<int:pk>', Inquiry_api_detail),

    path('CIP/<int:pk>', Comment_ip_api_list),




    path('FBN/', FreeNB_api_list),
    path('FBN/CRE/', FreeNB_api_create),
    path('FBN/<int:pk>', FreeNB_api_detail),

    path('CFR/<int:pk>', Comment_Free_api_list),
    path('CFR/', Comment_Free_api_create),
    path('CFR/DE/<int:pk>', Comment_Free_api_detail),


    path('suggest_fr/', suggestionFree_create),
    path('suggest_fr/<int:pk>', suggestionFree_count),





    path('suggest_st/', suggestionStory_create),
    path('suggest_st/<int:pk>', suggestionStory_count),


    path('SBN/', StoryNoticeBoard_api_list),
    path('SBN/CRE/', StoryNoticeBoard_api_Create),
    path('SBN/<int:pk>', StoryNoticeBoard_api_detail),

    path('CST/<int:pk>', Comment_Story_api_list),
    path('CST/', Comment_Story_api_create),
    path('CST/DE/<int:pk>', Comment_Story_api_detail),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
