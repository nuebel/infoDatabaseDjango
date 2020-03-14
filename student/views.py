from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Student

class DetailView(generic.DetailView):
	model = Student
	template_name = 'student/detail.html'

def index(request):
	student_list = Student.objects.order_by('last_name', 'first_name')
	context = {"student_list": student_list,}
	return render(request, 'student/index.html', context)

def add(request):
	return render(request, 'student/add.html')

def addNew(request):
	# Translate checkbox values to python booleans
	if request.POST.get('prospect') == 'true': prospect = True
	else: prospect = False
	if request.POST.get('info_card') == 'true': info_card = True
	else: info_card = False

	student = Student(
		first_name=request.POST['first_name'],
		last_name=request.POST['last_name'],
		school_year=request.POST['school_year'],
		gender=request.POST['gender'],
		color=request.POST['color'],
		prospect=prospect,
		phone=request.POST['phone'],
		email=request.POST['email'],
		info_card=info_card,
		major=request.POST['major'],
		church=request.POST['church'],
		other=request.POST['other']
		)

	student.save()

	return HttpResponseRedirect(reverse('student:detail', args=(student.id,)))
