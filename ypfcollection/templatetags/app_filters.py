from django import template
from datetime import date, timedelta

register = template.Library()

@register.simple_tag
def fee_per_person(fee, players):
    return fee/players