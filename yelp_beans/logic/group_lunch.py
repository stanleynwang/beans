# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import random

from yelp_beans.models import Restaurant


def generate_restaurant(match, group_size):
    count = Restaurant.query().order(-Restaurant.index).get().index + 1
    chosen_restaurant_id = random.randint(0, count)
    chosen_restaurant = Restaurant.query().filter(Restaurant.index == chosen_restaurant_id).get()
    return [chosen_restaurant]
