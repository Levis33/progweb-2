# Generated by Django 4.1.3 on 2022-11-02 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailTypes",
            fields=[
                ("email_type", models.IntegerField(primary_key=True, serialize=False)),
                ("description", models.CharField(max_length=150)),
                ("template_name", models.CharField(max_length=150)),
            ],
            options={"db_table": "email_types", "managed": True,},
        ),
        migrations.CreateModel(
            name="Log",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("ip", models.GenericIPAddressField()),
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "event",
                    models.IntegerField(
                        choices=[
                            (1, "Usuário fez login"),
                            (2, "Usuário fez logout"),
                            (3, "Usuário mudou a senha"),
                            (4, "Usuário criado"),
                            (5, "Usuário falhou no login"),
                            (6, "Usuário pediu redefinição de senha"),
                            (7, "Usuário redefiniu senha"),
                        ]
                    ),
                ),
                ("description", models.CharField(max_length=300, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
