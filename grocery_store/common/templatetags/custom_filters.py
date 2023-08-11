from django import template

register = template.Library()


@register.filter(name='check_group')
def check_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
