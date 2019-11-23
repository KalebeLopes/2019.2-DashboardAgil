# Generated by Django 2.2.7 on 2019-11-22 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Milestones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milestoneID', models.IntegerField()),
                ('state', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('due_on', models.DateTimeField()),
            ],
        ),
    ]