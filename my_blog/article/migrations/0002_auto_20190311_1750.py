# Generated by Django 2.1.7 on 2019-03-11 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_time']},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='date',
            new_name='date_time',
        ),
    ]