# Generated by Django 2.2.4 on 2019-10-23 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_boardcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardcomment',
            name='user',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='noticecomment',
            name='user',
            field=models.TextField(),
        ),
    ]
