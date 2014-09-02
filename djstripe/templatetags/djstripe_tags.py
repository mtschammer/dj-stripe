# -*- coding: utf-8 -*-
from __future__ import division

from django.template import Library
from djstripe.utils import get_djstripe_customer


register = Library()


@register.filter
def djdiv(value, arg):
    """
    Divide the value by the arg, using Python 3-style division that returns
    floats. If bad values are passed in, return the empty string.
    """

    try:
        return value / arg
    except (ValueError, TypeError):
        try:
            return value / arg
        except Exception:
            return ''
division.is_safe = False


@register.assignment_tag
def get_djstripe_customer_tag(user):
    return get_djstripe_customer(user)