from unittest.mock import Mock
##### TEST RESTURANT
from lib.resturants01 import *
'''
test resturant add entry
'''
def test_given_none_list_return_listempty():
    resturant_entry = Resturant()
    assert resturant_entry.resturants_list == []
    
def test_given_dishes_store_list():
    resturant_entry = Resturant()
    
    # entry dishes fake
    entryfake = Mock()
    entryfake.dish_name = "Spaghetti Carbonara"
    entryfake.dish_price = 23
    entryfake.cooking_time = 15    # minutes
    
    resturant_entry.add(entryfake)
    assert resturant_entry.resturants_list == [entryfake]

'''
test resturant add entries
'''
def test_given_dishes_store_list():
    resturant_entry3 = Resturant()
    
    # entry dishes fake
    entryfake3 = Mock()
    entryfake3.dish_name = "Spaghetti Carbonara"
    entryfake3.dish_price = 23
    entryfake3.cooking_time = 15    # minutes
    entryfake4 = Mock()
    entryfake4.dish_name = "Greek Salad"
    entryfake4.dish_price = 18
    entryfake4.cooking_time = 10    # minutes
    
    resturant_entry3.add(entryfake3)
    resturant_entry3.add(entryfake4)
    assert resturant_entry3.resturants_list == [entryfake3, entryfake4]

'''
return dishes list
'''
def test_given_dishes_get_list():
    resturant_entry1 = Resturant()
    
    # entry dishes fake
    entryfake5 = Mock()
    #entryfake1.dish_name = "Spaghetti Carbonara"
    #entryfake1.dish_price = 23
    #entryfake1.cooking_time = 15    # minutes
    entryfake6 = Mock()
    #entryfake2.dish_name = "Greek Salad"
    #entryfake2.dish_price = 18
    #entryfake2.cooking_time = 10    # minutes
    
    #resturant_entry.add(entryfake1)
    #resturant_entry.add(entryfake2)
    
    assert resturant_entry1.get_dishes() == [entryfake5, entryfake6]
    
    
###### TEST DISHES
from lib.dish01 import *
'''
list exist? class store result?
'''
def test_check_list_exist():
    dish_entry = Dish("Spaghetti Carbonara", 23, 15)
    assert dish_entry.dish_name == "Spaghetti Carbonara"