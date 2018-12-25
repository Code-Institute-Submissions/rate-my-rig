# Generated by Django 2.0 on 2018-12-24 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20181224_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_info',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='cpu',
            field=models.CharField(choices=[('i3 Gen-7', 'i3 Gen-7'), ('i3 Gen-8', 'i3 Gen-8'), ('i5 Gen-7', 'i5 Gen-7'), ('i5 Gen-8', 'i5 Gen-8'), ('i7 Gen-7', 'i7 Gen-7'), ('i7 Gen-8', 'i7 Gen-8'), ('i9 Gen-7', 'i9 Gen-7'), ('i9 Gen-8', 'i9 Gen-8'), ('Ryzen 3 Gen-1', 'Ryzen 3 Gen-1'), ('Ryzen 3 Gen-2', 'Ryzen 3 Gen-2'), ('Ryzen 5 Gen-1', 'Ryzen 5 Gen-1'), ('Ryzen 5 Gen-2', 'Ryzen 5 Gen-2'), ('Ryzen 7 Gen-1', 'Ryzen 7 Gen-1'), ('Ryzen 7 Gen-2', 'Ryzen 7 Gen-2'), ('Ryzen Threadripper Gen-1', 'Ryzen Threadripper Gen-1'), ('Ryzen Threadripper Gen-2', 'Ryzen Threadripper Gen-2')], default='i5 Gen-8', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='gpu',
            field=models.CharField(choices=[('GTX 1060', 'GTX 1060'), ('GTX 1060Ti', 'GTX 1060Ti'), ('GTX 1070', 'GTX 1070'), ('GTX 1070Ti', 'GTX 1070Ti'), ('GTX 1080', 'GTX 1080'), ('GTX 1080Ti', 'GTX 1080Ti'), ('GTX 2070', 'GTX 2070'), ('GTX 2070ti', 'GTX 2070Ti'), ('GTX 2080', 'GTX 2080'), ('GTX 2080Ti', 'GTX 2080Ti')], default='GTX 1080', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='ram',
            field=models.CharField(choices=[('4GB', '4GB'), ('8GB', '8GB'), ('16GB', '16GB'), ('32GB', '32GB'), ('64GB', '64GB'), ('128GB', '128GB')], default='8GB', max_length=20),
        ),
    ]