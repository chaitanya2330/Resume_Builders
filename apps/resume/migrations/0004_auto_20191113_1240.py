# Generated by Django 2.2.7 on 2019-11-13 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20191113_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumeitem',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
