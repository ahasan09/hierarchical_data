# hierarchical_data
Python Django MPTT

## Admin: safia
## Password: 1234

Build a simple Django server that uses MPTT models from django-mptt to create a Dropbox-esque web interface where you can create "folders" and "files" in an arbitrary structure and then display that structure. We won't actually be uploading anything, just making model instances and using them to represent real data. See the rubric for more detailed information.

### Steps:
1. pip install django-mptt
2. python `manage.py` makemigrations files
3. python `manage.py` migrate
4. pythom `manage.py` runserver