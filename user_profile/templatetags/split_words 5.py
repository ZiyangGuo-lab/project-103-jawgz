from django import template
from datetime import datetime, timezone, timedelta

register = template.Library()

@register.simple_tag
def split(value, arg):
    return value.split(arg)

@register.simple_tag
def calculatetime(value):

    difference = datetime.now(timezone.utc) - timedelta(hours=5) - value
    if difference.days > 0:
        if difference.days == 1:
            return "1 day ago"
        else:
            return str(difference.days) + " days ago"

    hours = int(float(difference.seconds / 3600))
    if hours >= 1:
        if hours == 1:
            return "1 hour ago"
        else:
            return str(hours) + " hours ago"

    minutes = int(float(difference.seconds / 60))
    if minutes <= 2:
        return "just now"
    else:
        return str(minutes) + " minutes ago"