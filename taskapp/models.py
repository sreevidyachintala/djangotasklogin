from django.db import models

# Create your models here.

# class Stu(models.Model):
# 	branches=[('CSE','CSE'),('EEE','EEE'),('ECE','ECE'),('IT','IT'),('CIVIL','CIVIL'),('Mech','Mech')]
# 	name=models.CharField(max_length=30)
# 	password=models.CharField(max_length=30,null=True)
# 	id1 =models.CharField(max_length=10)
# 	email=models.EmailField(max_length=30)
# 	collegename=models.CharField(max_length=10)
# 	department=models.CharField(max_length=20,choices=branches)


# class Fac(models.Model):
# 	branches=[('CSE','CSE'),('EEE','EEE'),('ECE','ECE'),('IT','IT'),('CIVIL','CIVIL'),('Mech','Mech')]
# 	name=models.CharField(max_length=30)
# 	password=models.CharField(max_length=30,null=True)
# 	id1 =models.CharField(max_length=10)
# 	email=models.EmailField(max_length=30)
# 	collegename=models.CharField(max_length=10)
# 	department=models.CharField(max_length=20,choices=branches)
# 	designation=models.CharField(max_length=30)

class StuFac(models.Model):
	branches=[('CSE','CSE'),('EEE','EEE'),('ECE','ECE'),('IT','IT'),('CIVIL','CIVIL'),('Mech','Mech')]
	#br=[('CSE','CSE'),('EEE','EEE'),('ECE','ECE'),('IT','IT'),('CIVIL','CIVIL'),('Mech','Mech')]
	name=models.CharField(max_length=30,null=True)
	password=models.CharField(max_length=30,null=True)
	rollno =models.CharField(max_length=10,null=True)
	email=models.EmailField(max_length=30,null=True)
	collegename=models.CharField(max_length=10,null=True)
	department=models.CharField(max_length=20,choices=branches,null=True)
	fac_name=models.CharField(max_length=30)
	fac_password=models.CharField(max_length=30,null=True)
	id1 =models.CharField(max_length=10)
	fac_email=models.EmailField(max_length=30)
	fac_collegename=models.CharField(max_length=10)
	fac_department=models.CharField(max_length=20,choices=branches)
	salary=models.IntegerField(null=True)
	designation=models.CharField(max_length=30)





