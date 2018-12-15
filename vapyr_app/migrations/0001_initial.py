# Generated by Django 2.0.8 on 2018-12-15 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('image', models.URLField(blank=True, max_length=150)),
                ('platform', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('rating', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='JoinTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefer', models.BooleanField()),
                ('wishlist', models.BooleanField()),
                ('gameKey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game', to='vapyr_app.Game')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('pref_platform', models.CharField(max_length=100)),
                ('gamer_style', models.CharField(choices=[('CASUAL', 'Casual'), ('HARDCORE', 'Hardcore'), ('PRO', 'Profesional')], default='HARDCORE', max_length=11)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='jointable',
            name='userKey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='vapyr_app.UserProfile'),
        ),
    ]