from ast import Add
from multiprocessing import context
from urllib.parse import urlunsplit
from django.urls import URLPattern, path
from django.views.generic import TemplateView

from home.views import AddGroup, AddStudent, AddTeacher, DeleteStudent, DeleteTeacher, GroupView, StudentView, UpdateGroup, DeleteGroup, HomeView, TeacherView, UpdateStudent, UpdateTeacher


urlpatterns  = [
    # path('', TemplateView.as_view(template_name = 'base.html')),
    path('', HomeView.as_view()),
    path('home/', HomeView.as_view()),
    
    path('group/', GroupView.as_view()),
    path('teacher/', TeacherView.as_view()),
    path('student/', StudentView.as_view()),

    path('group/search', GroupView.as_view(), name=''),
    path('teacher/search', TeacherView.as_view(), name=''),
    path('student/search', StudentView.as_view(), name=''),

    path('add-group/', AddGroup.as_view()),
    path('add-teacher/', AddTeacher.as_view()),
    path('add-student/', AddStudent.as_view()),

    path('<pk>/update-group/', UpdateGroup.as_view()),
    path('<pk>/update-teacher/', UpdateTeacher.as_view()),
    path('<pk>/update-student/', UpdateStudent.as_view()),

    path('<pk>/delete-teacher/', DeleteTeacher.as_view()),
    path('<pk>/delete-student/', DeleteStudent.as_view()),
    path('<pk>/delete-group/', DeleteGroup.as_view()),

]