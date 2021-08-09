from django import template

register = template.Library()

def cut(value,arg):
    #value is the value from context dictionary and arg is addtional argument needed
    """
    This cuts out all the values of arg from the string.
    """
    return value.replace(arg,'')

register.filter('cut',cut)
