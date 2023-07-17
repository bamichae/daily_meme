# Generated by Django 4.0.2 on 2022-02-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('is_daily_meme', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-uploaded_at'],
            },
        ),
    ]
