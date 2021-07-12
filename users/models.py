from django.db import models

# Create your models here.


class Users(models.Model):
	name=models.CharField(max_length=30)
	register_no= models.CharField(max_length=10)
	branch = models.CharField(max_length=20)
	email= models.CharField(max_length=50)
	password=models.CharField(max_length=20)
	con_password = models.CharField(max_length=20)


class Logins(models.Model):
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=20)


class Courses(models.Model):
	reg_no = models.CharField(max_length=30)
	branch = models.CharField(max_length=3)
	course = models.CharField(max_length=20)


class Chat(models.Model):
	reg_no = models.CharField(max_length = 30)
	message = models.TextField()
	posted_at = models.DateTimeField(auto_now=True,null=True)

class QuizBranch(models.Model):
	reg_no = models.CharField(max_length = 30)
	branch = models.CharField(max_length=10)


class Quiz(models.Model):
	branch = models.CharField(max_length=10,null=True)
	number = models.CharField(max_length=10,null=True)
	question = models.TextField()
	option_1 = models.TextField()
	option_2 = models.TextField()
	option_3 = models.TextField()
	option_4 = models.TextField()
	corranswer = models.TextField()

	class Meta:
		unique_together = (('branch','number'),)
		#unique_together = (("course", "id"),)


	def __str__(self):
		return str(self.option_1+','+self.option_2+','+self.option_3+','+self.option_4)

class evaluation(models.Model):
	reg_no = models.CharField(max_length=30)
	branch = models.CharField(max_length=10)
	marks = models.CharField(max_length=20)
	posted_at = models.DateTimeField(auto_now=True,null=True)

