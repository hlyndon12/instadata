# Generated by Django 3.2.3 on 2021-05-20 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210520_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='category',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='category',
            field=models.ManyToManyField(to='main.Categories'),
        ),
    ]
