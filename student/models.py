from django.db import models

class Student(models.Model):
	FRESHMAN = 'FR'
	SOPHOMORE = 'SO'
	JUNIOR = 'JR'
	SENIOR = 'SR'
	GRAD = 'GR'
	YEAR_IN_SCHOOL_CHOICES = [
		(FRESHMAN, 'Freshman'),
		(SOPHOMORE, 'Sophomore'),
		(JUNIOR, 'Junior'),
		(SENIOR, 'Senior'),
		(GRAD, 'Grad School'),
	]

	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOICES = [
		(MALE, 'Male'),
		(FEMALE, 'Female'),
	]

	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	school_year = models.CharField(
		max_length=2,
		choices=YEAR_IN_SCHOOL_CHOICES,
		default=FRESHMAN,
	)
	gender = models.CharField(
		max_length=1,
		choices = GENDER_CHOICES,
		default=MALE
	)
	color = models.CharField(max_length=32, default="none")
	phone = models.CharField(max_length=12, blank=True)
	email = models.EmailField(blank=True)
	on_campus = models.BooleanField(default=False)
	local_street_num = models.CharField(max_length=32, blank=True)
	local_street = models.CharField(max_length=128, blank=True)
	perm_street_num = models.CharField(max_length=32, blank=True)
	perm_street = models.CharField(max_length=128, blank=True)
	perm_city = models.CharField(max_length=64, blank=True)
	perm_state = models.CharField(max_length=2, blank=True)
	perm_zip = models.CharField(max_length=10, blank=True)
	major = models.CharField(max_length=64, blank=True)
	church = models.CharField(max_length=64, blank=True)
	prospect = models.BooleanField(default=False)
	info_card = models.BooleanField(default=False)
	other = models.CharField(max_length=254, blank=True)

	def __str__(self):
		return self.first_name + " " + self.last_name
