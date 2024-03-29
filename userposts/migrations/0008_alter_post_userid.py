# Generated by Django 4.0.4 on 2022-05-31 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_remove_usermodel_user_remove_usermodel_userid_and_more"),
        ("userposts", "0007_alter_post_userid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="userID",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="userID",
                to="users.usermodel",
            ),
        ),
    ]
