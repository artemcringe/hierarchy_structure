from django.db import models


class Worker(models.Model):
    class Position(models.TextChoices):
        OPERATOR = "OPER", "Operator"
        LEADING_SPECIALIST = "LEAD", "Leading Specialist"
        DIRECTOR_OF_DEPARTMENT = "DIR_DEP", "Director of Department"
        DEPARTMENT_HEAD = "HEAD_DEP", "Department head"
        CHIEF_DIRECTOR = "CHIEF", "Chief Director"

    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)
    position = models.CharField(max_length=30,
                                choices=Position.choices,
                                default=Position.OPERATOR
                                )
    employment_date = models.DateField()
    salary = models.PositiveIntegerField()
    boss = models.ForeignKey("Worker", on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f"{self.surname} {self.name} {self.position}"