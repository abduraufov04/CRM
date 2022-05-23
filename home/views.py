from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from home.models import Group, Student, Teacher
from django.db.models import Q

class HomeView(ListView):
    model = Group
    template_name = 'index.html'
    context_object_name = 'gruop_list'


class GroupView(ListView):
    model = Group
    template_name = 'group.html'
    def get_context_data(self, **kwargs):
        q = Group.objects.all()
        print(q)
        search = self.request.GET
        if 'group' in search :
            q = q.filter(Q(name__icontains = search['group']) | Q(price__icontains = search['group']) | Q(create_date__icontains = search['group']) | Q(direction__icontains = search['group']))

        context = {'gruop_list' : q}
        return context



class TeacherView(ListView):
    model = Teacher
    template_name = 'teacher.html'
    
    def get_context_data(self, **kwargs):
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

        context = {'teacher_list' : q}
        return context


class StudentView(ListView):
    model = Student
    template_name = 'student.html'
    
    def get_context_data(self, **kwargs):
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

        context = {'student_list' : q}
        return context


class AddGroup(CreateView):
    model = Group
    fields = ['name', 'direction', 'price']
    template_name = 'add-group.html'
    success_url = '/group/'


class UpdateGroup(UpdateView):
    model = Group
    fields = ['name', 'direction', 'price']
    template_name = 'add-group.html'
    success_url = '/group/'


class DeleteGroup(DeleteView):
    model = Group
    template_name = 'group_confirm_delete.html'
    success_url = '/group/'


class AddTeacher(CreateView):
    model = Teacher
    fields = ['name', 'surname', 'age', 'region', 'district', 'groups']
    template_name = 'add-teacher.html'
    success_url = '/teacher/'


class UpdateTeacher(UpdateView):
    model = Teacher
    fields = ['name', 'surname', 'age', 'region', 'district', 'groups']
    template_name = 'add-teacher.html'
    success_url = '/teacher/'


class DeleteTeacher(DeleteView):
    model = Teacher
    template_name = 'teacher_confirm_delete.html'
    success_url = '/teacher/'


class AddStudent(CreateView):
    model = Student
    fields = ['name', 'surname', 'age', 'region', 'district', 'groups']
    template_name = 'add-teacher.html'
    success_url = '/student/'


class UpdateStudent(UpdateView):
    model = Student
    fields = ['name', 'surname', 'age', 'region', 'district', 'groups']
    template_name = 'add-teacher.html'
    success_url = '/student/'


class DeleteStudent(DeleteView):
    model = Student
    template_name = 'teacher_confirm_delete.html'
    success_url = '/student/'