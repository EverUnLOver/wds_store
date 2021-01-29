# Generated by Django 3.0.11 on 2021-01-29 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camisa',
            fields=[
                ('id', models.AutoField(auto_created=True, error_messages={'unique': 'Ya esta esa id.'}, primary_key=True, serialize=False, unique=True)),
                ('tipo', models.CharField(choices=[('HOMBRE', 'Hombre'), ('MUJER', 'Mujer'), ('NIÑA', 'Niña'), ('NIÑO', 'Niño')], max_length=7)),
            ],
            options={
                'ordering': ['tipo', '-id'],
            },
        ),
    ]