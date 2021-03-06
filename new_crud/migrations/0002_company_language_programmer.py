# Generated by Django 3.0 on 2020-08-13 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=54)),
                ('location', models.CharField(max_length=54)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=54)),
                ('creator', models.CharField(max_length=54)),
                ('paradigm', models.CharField(max_length=54)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=54)),
                ('age', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_crud.Company')),
                ('language', models.ManyToManyField(to='new_crud.Language')),
            ],
        ),
    ]
