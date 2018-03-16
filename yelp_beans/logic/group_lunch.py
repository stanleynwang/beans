# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from yelp_beans.models import Restaurant


def generate_restaurant(match, group_size):
    return [Restaurant(name="Tenmatsu", address="336 Kearny St, San Francisco, CA 94108")]
