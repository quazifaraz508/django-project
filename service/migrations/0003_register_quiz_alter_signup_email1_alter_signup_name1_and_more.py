# Generated by Django 5.0.6 on 2024-06-22 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register_quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('birthday', models.DateField()),
                ('fname2', models.CharField(max_length=100)),
                ('gender2', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('birthday2', models.DateField()),
                ('fname3', models.CharField(max_length=100)),
                ('gender3', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('birthday3', models.DateField()),
                ('Collage', models.CharField(choices=[('Anjuman Engg', 'Anjuman Engg'),('Anjuman Poly', 'Anjuman Poly'),('Other', 'Other')],max_length=100)),
                ('Contact_no', models.CharField(max_length=10)),
            ]
        )
        
    ]