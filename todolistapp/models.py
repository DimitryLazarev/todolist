from django.db import models


class ToDoList(models.Model):
    text = models.CharField(max_length=255)
    position = models.IntegerField()
    priority = models.CharField(max_length=10)
    readiness = models.BooleanField()


class ToDoListFiltered(models.Model):
    text = models.CharField(max_length=255)
    position = models.IntegerField()
    priority = models.CharField(max_length=10)
    readiness = models.BooleanField()
    todolist = models.OneToOneField(
        'ToDoList',
        null=False,
        on_delete=models.CASCADE,
        related_name='filtered_note',
    )

