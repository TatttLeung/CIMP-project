# Generated by Django 3.1.2 on 2020-10-27 09:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.PositiveIntegerField()),
                ('pid', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.PositiveIntegerField()),
                ('Tea', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubdate', models.DateTimeField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=2000)),
                ('thumbupcount', models.PositiveIntegerField(default=0)),
                ('status', models.PositiveIntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubdate', models.DateTimeField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=2000)),
                ('status', models.PositiveIntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubdate', models.DateTimeField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=2000)),
                ('status', models.PositiveIntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
