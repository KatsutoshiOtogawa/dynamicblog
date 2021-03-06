# Generated by Django 3.1 on 2020-09-03 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20200904_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarent',
            name='tarent_body',
            field=models.ManyToManyField(blank=True, null=True, to='api.TarentBody', verbose_name='ボディ'),
        ),
        migrations.AlterField(
            model_name='tarent',
            name='tarent_face',
            field=models.ManyToManyField(blank=True, null=True, to='api.TarentFace', verbose_name='顔の傾向'),
        ),
        migrations.AlterField(
            model_name='tarent',
            name='tarent_lower_body',
            field=models.ManyToManyField(blank=True, null=True, to='api.TarentLowerBody', verbose_name='下半身'),
        ),
        migrations.AlterField(
            model_name='tarent',
            name='tarent_personality',
            field=models.ManyToManyField(blank=True, null=True, to='api.TarentPersonality', verbose_name='性格(こっちから見えるでよい。)'),
        ),
        migrations.AlterField(
            model_name='tarent',
            name='tarent_upper_body',
            field=models.ManyToManyField(blank=True, null=True, to='api.TarentUpperBody', verbose_name='上半身'),
        ),
    ]
