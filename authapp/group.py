from django.contrib.auth.models import Group

GROUPS = ['admin', 'anonymous']
MODELS = ['User']

for group in GROUPS:
    new_group, created = Group.objects.get_or_create(name=group)