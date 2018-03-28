# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import mock
import pytest

from yelp_beans.enums import ActivityType
from yelp_beans.logic.group_lunch import generate_restaurant_picks
from yelp_beans.logic.group_lunch import is_lunch_match
from yelp_beans.models import Restaurant


@pytest.mark.parametrize(
    'lunch_type,expected',
    [(ActivityType.basic.value, False), (ActivityType.lunch.value, True)],
)
def test_is_lunch_match(lunch_type, expected):
    assert is_lunch_match(lunch_type) == expected


def test_generate_restaurant_picks_gets_existing_restaurants(minimal_database):
    restaurant_key_1 = Restaurant(
        index=0,
        name='fake restaurant',
        address='address',
        photo_url='photo_url',
        yelp_url='yelp_url',
        phone_number='phone_number',
    ).put()
    Restaurant(
        index=1,
        name='fake restaurant 2',
        address='address',
        photo_url='photo_url',
        yelp_url='yelp_url',
        phone_number='phone_number',
    ).put()
    with mock.patch('random.randint', return_value=0):
        picks = generate_restaurant_picks([mock.Mock()])
    assert len(picks) == 1
    assert picks[0].key == restaurant_key_1


def test_generate_restaurant_picks_gets_equal_number_of_picks(minimal_database):
    Restaurant(
        index=0,
        name='fake restaurant',
        address='address',
        photo_url='photo_url',
        yelp_url='yelp_url',
        phone_number='phone_number',
    ).put()
    picks = generate_restaurant_picks([mock.Mock(), mock.Mock(), mock.Mock()])
    assert len(picks) == 3
