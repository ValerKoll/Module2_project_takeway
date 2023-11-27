from unittest.mock import Mock
from lib.takeawayApp import *

def test_add_resturants():
    app = TakeawayApp()
    #maock
    fakeresturant = Mock()
    
    #aspected
    app.add(fakeresturant)
    #result
    app.resturants_list
    #assert
    
    