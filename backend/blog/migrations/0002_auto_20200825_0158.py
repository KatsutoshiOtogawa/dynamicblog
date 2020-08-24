# Generated by Django 3.1 on 2020-08-24 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='サイトタイプ')),
            ],
        ),
        migrations.CreateModel(
            name='TarentArt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='作品名')),
                ('published_date', models.DateField(verbose_name='出版日')),
            ],
        ),
        migrations.CreateModel(
            name='TarentArtFetishism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='作品名')),
                ('published_date', models.DateField(verbose_name='出版日')),
            ],
        ),
        migrations.CreateModel(
            name='TarentBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='ボディ')),
            ],
        ),
        migrations.CreateModel(
            name='TarentBraSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2, verbose_name='ブラのサイズ')),
            ],
        ),
        migrations.CreateModel(
            name='TarentFace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='顔の傾向')),
            ],
        ),
        migrations.CreateModel(
            name='TarentLowerBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='下半身')),
            ],
        ),
        migrations.CreateModel(
            name='TarentPersonality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='性格(こっちから見えるでよい。)')),
            ],
        ),
        migrations.CreateModel(
            name='TarentSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='url')),
                ('site_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.sitetype', verbose_name='タレント')),
            ],
        ),
        migrations.CreateModel(
            name='TarentUpperBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='上半身')),
            ],
        ),
        migrations.AddField(
            model_name='tarent',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='誕生日(分からなければ空欄)'),
        ),
        migrations.AddField(
            model_name='tarent',
            name='charm_point',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='良い点👍'),
        ),
        migrations.AlterField(
            model_name='tarenttimeline',
            name='draft',
            field=models.BooleanField(default=True, verbose_name='下書き(チェックを外すと公開されます。)'),
        ),
        migrations.AlterField(
            model_name='tarenttimeline',
            name='price',
            field=models.IntegerField(verbose_name='価格'),
        ),
        migrations.DeleteModel(
            name='TarentSNS',
        ),
        migrations.AddField(
            model_name='tarentsite',
            name='tarent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.tarent', verbose_name='タレント'),
        ),
        migrations.AddField(
            model_name='tarentartfetishism',
            name='tarent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.tarent', verbose_name='タレント'),
        ),
        migrations.AddField(
            model_name='tarentart',
            name='tarent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.tarent', verbose_name='タレント'),
        ),
    ]
