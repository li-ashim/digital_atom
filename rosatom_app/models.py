from django.db import models
from django.db.models.deletion import PROTECT, CASCADE
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)

    fullname = models.CharField(max_length=80, verbose_name='ФИО', db_index=True)
    department = models.CharField(max_length=80, verbose_name='Отдел')
    position = models.CharField(max_length=80, verbose_name='Должность')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField()

    class Meta:
        abstract = True
        ordering = ['fullname']

    def __str__(self):
        return self.fullname


class Mentor(Employee):
    class Meta(Employee.Meta):
        abstract = False
        verbose_name = 'Наставник'
        verbose_name_plural = 'Наставники'


class Novice(Employee):

    salary = models.IntegerField(verbose_name='Заплата', null=True)
    schedule = models.TextField(verbose_name='График')
    workplace = models.TextField(verbose_name='Рабочее место')

    mentor = models.OneToOneField(Mentor, on_delete=PROTECT)

    class Meta(Employee.Meta):
        abstract = False
        verbose_name = 'Новичок'
        verbose_name_plural = 'Новички'
        

class Task(models.Model):
    task_name = models.CharField(max_length=40, verbose_name='Задача')
    content = models.TextField(verbose_name='Содержание')
    deadline = models.DateTimeField(verbose_name='Дедлайн', db_index=True)
    novice = models.ForeignKey(Novice, on_delete=CASCADE, db_index=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['deadline']

    def __str__(self):
        return self.task_name


class UsefulMaterial(models.Model):
    material_type = models.CharField(max_length=20, verbose_name='Тип')
    department = models.CharField(max_length=80, verbose_name='Отдел', null=True)
    title = models.CharField(max_length=80, verbose_name='Заголовок')
    author = models.CharField(max_length=80, verbose_name='Автор')
    description = models.TextField(verbose_name='Описание')
    date_added = models.DateTimeField(verbose_name='Добавлено', 
                                auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Полезный материал'
        verbose_name_plural = 'Полезные материалы'
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title

    
class Colleague(models.Model):
    # image = models.ImageField()
    fullname = models.CharField(max_length=80, verbose_name='ФИО', db_index=True)
    department = models.CharField(max_length=80, verbose_name='Отдел')
    position = models.CharField(max_length=80, verbose_name='Должность')
    email = models.EmailField()

    class Meta:
        ordering = ['fullname']

    def __str__(self):
        return self.fullname