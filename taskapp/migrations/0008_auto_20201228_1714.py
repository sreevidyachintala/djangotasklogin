# Generated by Django 3.1.4 on 2020-12-28 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0007_auto_20201228_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stufac',
            old_name='stu_collegename',
            new_name='collegename',
        ),
        migrations.RenameField(
            model_name='stufac',
            old_name='stu_department',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='stufac',
            old_name='stu_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='stufac',
            old_name='stu_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='stufac',
            old_name='stu_password',
            new_name='password',
        ),
    ]