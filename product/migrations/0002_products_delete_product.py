# Generated by Django 4.0.6 on 2022-07-13 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.FloatField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
