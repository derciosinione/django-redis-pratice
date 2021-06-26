# Generated by Django 3.2.3 on 2021-06-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('age', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
