# Generated by Django 3.2 on 2021-06-17 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_mangas_webcomics', '0002_auto_20210617_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='chapter_text',
            new_name='chapter',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='image_text',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='link_text',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='title_text',
            new_name='title',
        ),
    ]