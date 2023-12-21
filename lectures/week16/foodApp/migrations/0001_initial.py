# Generated by Django 5.0 on 2023-12-20 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('meal', models.CharField(max_length=255)),
                ('servings', models.IntegerField(default=1)),
            ],
        ),
    ]
