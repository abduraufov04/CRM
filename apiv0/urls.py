from django.urls import path

from apiv0.views import GroupCreateList, GroupDeleteList, GroupUpdateList, GroupViewSet, StudentCreateList, StudentDeleteList, StudentUpdateList, StudentViewSet, TeacherCreateList, TeacherDeleteList, TeacherUpdateList, TeacherViewSet

urlpatterns = [
    path('group/', GroupViewSet.as_view({'get' : 'list'})),
    path('teacher/', TeacherViewSet.as_view({'get' : 'list'})),
    path('student/', StudentViewSet.as_view({'get' : 'list'})),
    
    path('group/search', GroupViewSet.as_view({'get' : 'list'})),
    path('teacher/search', TeacherViewSet.as_view({'get' : 'list'})),
    path('student/search', StudentViewSet.as_view({'get' : 'list'})),

    path('group/create/', GroupCreateList.as_view()),
    path('teacher/create/', TeacherCreateList.as_view()),
    path('student/create/', StudentCreateList.as_view()),

    path('group/update/', GroupUpdateList.as_view()),
    path('teacher/update/', TeacherUpdateList.as_view()),
    path('student/update/', StudentUpdateList.as_view()),

    path('group/delete/', GroupDeleteList.as_view()),
    path('teacher/delete/', TeacherDeleteList.as_view()),
    path('student/delete/', StudentDeleteList.as_view()),

]