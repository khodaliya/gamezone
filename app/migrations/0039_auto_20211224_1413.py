# Generated by Django 3.2.7 on 2021-12-24 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_auto_20211224_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='contant',
        ),
        migrations.AddField(
            model_name='product',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='catagory',
            field=models.CharField(blank=True, choices=[('GC', 'Gaming Computers'), ('GM', 'Gaming Mobile'), ('GL', 'Gaming Laptops'), ('CPU', 'Gaming CPU'), ('GMT', 'Gaming Moniter'), ('GH', 'Gaming Headphones'), ('M', 'Mouse'), ('K', 'Keybord'), ('KM', 'Keybord Mouse')], max_length=3, null=True),
        ),
    ]
