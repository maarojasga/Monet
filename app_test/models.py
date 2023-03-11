from django.db import models
from django.contrib.auth.models import User

# Información básica de los estudiantes
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10, unique=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.student_id

# Información básica de los exámenes
class Test(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

# Información d elas preguntas y su relación con los exámenes
class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

# Información de las respuesta realcionadas con los estudiantes, los exámenes y las preguntas
class Answer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.student.username} - {self.test.title} - {self.question.text}'