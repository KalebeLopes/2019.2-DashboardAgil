# Generated by Django 2.2.7 on 2019-11-22 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shaCommit', models.CharField(max_length=60)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
