from django.shortcuts import render
from home.models import *
from .serializer import *
from rest_framework import viewsets
from django.db.models import Q
from rest_framework import generics

# Create your views here.
class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer

    def get_queryset(self):
        q = Group.objects.all()
        search = self.request.GET
        if 'group' in search :
            q = q.filter(Q(name__icontains = search['group']) | Q(price__icontains = search['group']) | Q(create_date__icontains = search['group']) | Q(direction__icontains = search['group']))
        return q



class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_queryset(self):
        q = Teacher.objects.all()
        search = self.request.GET

        if 'name' in search :
            q = q.filter(name__icontains = search['name'])

        if 'surname' in search and search['surname']:
            q = q.filter(surname__icontains = search['surname'])
        
        if 'age' in search and search['age']:
            q = q.filter(age = search['age'])
        
        if 'group' in search and search['group']:
            q = q.filter(groups__name = search['group'])
        
        if 'address' in search and search['address']:
            q = q.filter(Q(region__name__icontains = search['address']) | Q(district__name__icontains = search['address']))

        
        return q


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        q = Student.objects.all()
        search = self.request.GET

        if 'name' in search :
            q = q.filter(name__icontains = search['name'])

        if 'surname' in search and search['surname']:
            q = q.filter(surname__icontains = search['surname'])
        
        if 'age' in search and search['age']:
            q = q.filter(age = search['age'])
        
        if 'group' in search and search['group']:
            q = q.filter(groups__name = search['group'])
        
        if 'address' in search and search['address']:
            q = q.filter(Q(region__name__icontains = search['address']) | Q(district__name__icontains = search['address']))

        return q

class GroupCreateList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TeacherCreateList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentCreateList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GroupUpdateList(generics.UpdateAPIView):
    serializer_class = GroupSerializer

    def get_object(self):
        return Group.objects.get(id = self.request.data.get('id'))


class TeacherUpdateList(generics.UpdateAPIView):
    serializer_class = TeacherSerializer

    def get_object(self):
        return Teacher.objects.get(id = self.request.data.get('id'))


class StudentUpdateList(generics.UpdateAPIView):
    serializer_class = StudentSerializer

    def get_object(self):
        return Student.objects.get(id = self.request.data.get('id'))


class GroupDeleteList(generics.DestroyAPIView):
    serializer_class = GroupSerializer
    
    def get_object(self):
        return Group.objects.get(pk = self.request.data.get('id'))



class TeacherDeleteList(generics.DestroyAPIView):
    serializer_class = TeacherSerializer
    
    def get_object(self):
        return Teacher.objects.get(pk = self.request.data.get('id'))


class StudentDeleteList(generics.DestroyAPIView):
    serializer_class = StudentSerializer
    
    def get_object(self):
        return Student.objects.get(pk = self.request.data.get('id'))