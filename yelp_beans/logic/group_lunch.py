# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import random

from yelp_beans.models import Restaurant


def generate_restaurant_picks(matches):
    max_id = Restaurant.query().order(-Restaurant.index).get().index
    picks = []
    for _ in matches:
        chosen_restaurant_id = random.randint(0, max_id)
        chosen_restaurant = Restaurant.query().filter(Restaurant.index == chosen_restaurant_id).get()
        picks.append(chosen_restaurant)
    return picks
