# Generated by Django 3.1 on 2020-09-04 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20200904_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='javpop',
            old_name='download_link',
            new_name='video',
        ),
        migrations.AlterField(
            model_name='javpopvideoimage',
            name='image',
            field=models.BinaryField(blank=True, editable=True, null=True, verbose_name='画像'),
        ),
    ]