from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import logging

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

def edit(request, pk):
	student = get_object_or_404(Student, pk=pk)
	context = {"student": student,}
	return render(request, 'student/edit.html', context)

def makeEdits(request):
	# Translate checkbox values to python booleans
	if request.POST.get('prospect') == 'true': prospect = True
	else: prospect = False
	if request.POST.get('info_card') == 'true': info_card = True
	else: info_card = False

	student = Student.objects.get(pk=request.POST['id'])
	student.first_name=request.POST['first_name']
	student.last_name=request.POST['last_name']
	student.school_year=request.POST['school_year']
	student.gender=request.POST['gender']
	student.color=request.POST['color']
	student.prospect=prospect
	student.phone=request.POST['phone']
	student.email=request.POST['email']
	student.info_card=info_card
	student.major=request.POST['major']
	student.church=request.POST['church']
	student.other=request.POST['other']

	student.save()

	return HttpResponseRedirect(reverse('student:detail', args=(student.id,)))

def delete(request, pk):
	student = get_object_or_404(Student, pk=pk)
	student.delete()

	student_list = Student.objects.order_by('last_name', 'first_name')
	context = {"student_list": student_list,}
	return render(request, 'student/index.html', context)

def search(request):
	search_by = request.POST['search_field']
	search_text = request.POST['search_text']
	logger = logging.getLogger('django')
	logger.info('In search')

	if search_by =='last_name':
		student_list = Student.objects.filter(last_name__icontains = search_text).order_by('last_name', 'first_name')
		message = 'Search for students with last name ' + search_text
	elif search_by == 'first_name':
		student_list = Student.objects.filter(first_name__icontains = search_text).order_by('last_name', 'first_name')
		message = 'Search for students with first name ' + search_text
	elif search_by == 'email':
		student_list = Student.objects.filter(email__icontains = search_text).order_by('last_name', 'first_name')
		message = 'Search for students with email ' + search_text
	elif search_by == 'color':
		student_list = Student.objects.filter(color__icontains = search_text).order_by('last_name', 'first_name')
		message = 'Search for students in ' + search_text + ' family'
	elif search_by == 'school_year':
		student_list = Student.objects.filter(school_year__icontains = search_text).order_by('last_name', 'first_name')
		message = 'Search for students in class ' + search_text
	elif search_by == 'dorm':
		student_list = Student.objects.filter(last_name__icontains = search_text).order_by('last_name', 'first_name')
		message = 'Search for students with last name ' + search_text
	elif search_by == 'homeAdd':
		student_list = Student.objects.filter(last_name__icontains = search_text).order_by('last_name', 'first_name')
		message = 'Search for students with last name ' + search_text
	elif search_by == 'major':
		student_list = Student.objects.filter(major__icontains = search_text).order_by('last_name', 'first_name')
		message = 'Search for students with major ' + search_text
	elif search_by == 'church':
		student_list = Student.objects.filter(church__icontains = search_text).order_by('last_name', 'first_name')
		message = 'Search for students with church ' + search_text
	elif search_by == 'other':
		student_list = Student.objects.filter(other__icontains = search_text).order_by('last_name', 'first_name')
		message = 'Search for students with notes ' + search_text
	else:
		message = 'No search field specified'

	context = {
		"student_list": student_list,
		"message": message,
		}

	return render(request, 'student/search.html', context)

def ajax_searchsort(request):
	logger = logging.getLogger('django')

	search_by = request.GET['search_field']
	search_text = request.GET['search_text']
	sort_by = request.GET['sort_by']
	logger.info('Searching for ' + search_text + ' in ' + search_by + ' sorted by ' + sort_by)

	if sort_by == 'last_name':
		sort_by_list = ['last_name', 'first_name']
		message = 'Sorted by Last Name'
	elif sort_by == 'first_name':
		sort_by_list = ['first_name', 'last_name']
		message = 'Sorted by First Name'
	elif sort_by == 'school_year':
		sort_by_list = ['school_year', 'last_name', 'first_name']
		message = 'Sorted by Class'
	elif sort_by == 'color':
		sort_by_list = ['color', 'last_name', 'first_name']
		message = 'Sorted by Family Group'
	elif sort_by == 'address':
		sort_by_list = ['last_name', 'first_name']
		message = 'Sorted by Address (not implemented yet)'

	if search_text == '':
		student_list = Student.objects.all().order_by(*sort_by_list)
		message = 'Search for all students - ' + message
	elif search_by =='last_name':
		student_list = Student.objects.filter(last_name__icontains = search_text).order_by(*sort_by_list)
		message = 'Search for students with last name ' + search_text + " - " + message
	elif search_by == 'first_name':
		student_list = Student.objects.filter(first_name__icontains = search_text).order_by(*sort_by_list)
		message = 'Search for students with first name ' + search_text + ' - ' + message
	elif search_by == 'email':
		student_list = Student.objects.filter(email__icontains = search_text).order_by(*sort_by_list)
		message = 'Search for students with email ' + search_text + ' - ' + message
	elif search_by == 'color':
		student_list = Student.objects.filter(color__icontains = search_text).order_by(*sort_by_list)
		message = 'Search for students in ' + search_text + ' family' + ' - ' + message
	elif search_by == 'school_year':
		student_list = Student.objects.filter(school_year__icontains = search_text).order_by(*sort_by_list)
		message = 'Search for students in class ' + search_text + ' - ' + message
	elif search_by == 'dorm':
		student_list = Student.objects.filter(last_name__icontains = search_text).order_by(*sort_by_list)
		message = 'Search for students with last name ' + search_text + ' - ' + message
	elif search_by == 'homeAdd':
		student_list = Student.objects.filter(last_name__icontains = search_text).order_by(*sort_by_list)
		message = 'Search for students with last name ' + search_text + ' - ' + message
	elif search_by == 'major':
		student_list = Student.objects.filter(major__icontains = search_text).order_by(*sort_by_list)
		message = 'Search for students with major ' + search_text + ' - ' + message
	elif search_by == 'church':
		student_list = Student.objects.filter(church__icontains = search_text).order_by(*sort_by_list)
		message = 'Search for students with church ' + search_text + ' - ' + message
	elif search_by == 'other':
		student_list = Student.objects.filter(other__icontains = search_text).order_by(*sort_by_list)
		message = 'Search for students with notes ' + search_text + ' - ' + message

	htmltext = '<h4>' + message + ': ' + str(len(student_list)) + ' Results</h4>'
	htmltext += '<table><tr><th colspan="2">Name</th><th>Email</th><th>Phone</th><th>School Address</th><th>Family</th><th>Class</th></tr>'

	for i, student in enumerate(student_list):
		if i%2 == 0: htmltext += '<tr class="shaded">'
		else: htmltext += '<tr>'

		htmltext += '<td>' + student.first_name + '</td><td>' + student.last_name + '</td><td>' + student.email + '</td><td>' + student.phone + '</td><td>' + student.local_street_num + '&nbsp;' + student.local_street + '</td><td>' + student.color + '</td><td>' + student.school_year + '</td></tr>'

	htmltext += '</table>'

	return HttpResponse(htmltext)
