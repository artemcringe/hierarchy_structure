from django.db import models


class Worker(models.Model):
    class Position(models.TextChoices):
        level_5 = "level_5", "5 level"
        level_4 = "level_4", "4 level"
        level_3 = "level_3", "3 level"
        level_2 = "level_2", "2 level"
        level_1 = "level_1", "1 level"

    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)
    position = models.CharField(max_length=30,
                                choices=Position.choices,
                                )
    employment_date = models.DateField()
    salary = models.PositiveIntegerField()
    boss = models.ForeignKey("Worker", on_delete=models.SET_NULL, null=True, blank=True, related_name="children")

    def __str__(self):
        return f"{self.name} {self.surname} {self.position}"


