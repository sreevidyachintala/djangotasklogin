# Generated by Django 3.1.4 on 2020-12-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0004_stufac'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Fac',
        ),
        migrations.DeleteModel(
            name='Stu',
        ),
        migrations.RemoveField(
            model_name='stufac',
            name='password',
        ),
        migrations.AddField(
            model_name='stufac',
            name='salary',
            field=models.IntegerField(null=True),
        ),
    ]