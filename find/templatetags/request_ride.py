from django import template

register = template.Library()

@register.simple_tag
def get_something(customer, business):
    print(customer)
    print(business)
    return "hello"


@register.filter(name='split')
def split(value, arg):
    print(value.split(arg))
    res = []
    for val in value.split(arg):
        if len(val) > 0:
            res.append(val)
    return res

