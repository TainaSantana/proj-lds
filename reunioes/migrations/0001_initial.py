# Generated by Django 3.0.8 on 2020-07-28 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reuniao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('descricao', models.TextField()),
                ('pauta', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
