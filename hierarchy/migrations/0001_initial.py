# Generated by Django 4.1.5 on 2023-01-23 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Worker",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("surname", models.CharField(max_length=40)),
                ("patronymic", models.CharField(max_length=40)),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("level_5", "5 level"),
                            ("level_4", "4 level"),
                            ("level_3", "3 level"),
                            ("level_2", "2 level"),
                            ("level_1", "1 level"),
                        ],
                        default="level_5",
                        max_length=30,
                    ),
                ),
                ("employment_date", models.DateField()),
                ("salary", models.PositiveIntegerField()),
                (
                    "boss",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="hierarchy.worker",
                    ),
                ),
            ],
        ),
    ]