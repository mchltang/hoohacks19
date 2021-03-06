# Generated by Django 2.1.7 on 2019-03-02 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(max_length=200)),
                ('floor', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=100)),
                ('size', models.IntegerField(default=1)),
                ('noise', models.CharField(default='average', max_length=7)),
                ('pub_date', models.DateTimeField(verbose_name='Date added')),
                ('notes', models.CharField(max_length=500)),
            ],
        ),
    ]
