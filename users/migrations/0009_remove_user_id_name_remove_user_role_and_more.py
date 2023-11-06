# Generated by Django 4.2.3 on 2023-11-06 17:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_id_name_user_role_alter_user_verification_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_key',
            field=models.TextField(blank=True, null=True, verbose_name=uuid.UUID('eb16de89-79ef-43e5-ac72-aabe27ffd5b8')),
        ),
    ]
