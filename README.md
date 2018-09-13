# django-infinite-migrations
A Django bug where removing model Meta option `default_related_name` causes infinite migrations.

Go ahead and clone this project and run multiple times:

```shell
./manage.py makemigrations
```

This will cause the command to generate migration again and again for this change:

```
migrations.AlterField(
    model_name='child',
    name='parent',
    field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Parent'),
),
```

which already exists in migration `0002_auto_20180913_2236.py`.
