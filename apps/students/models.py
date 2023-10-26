from django.db import models

# Create your models here.


class City(models.Model):
    namecity = models.CharField(max_length=100, verbose_name="Nome")
    acronym = models.CharField(max_length=10, verbose_name="Sigla Estado")

    def __str__(self) -> str:
        return self.namecity

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField()
    birthday = models.DateField()
    address = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Cidade")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Curso")

    def __str__(self) -> str:
        return self.name
