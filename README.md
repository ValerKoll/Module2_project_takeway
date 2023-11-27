# TakeAway App

github remote links:
git remote add origin https://github.com/ValerKoll/Module2_project_takeway.git
git branch -M main
git push -u origin main

### Request
Here is a project to test your golden square skills overall:

> As a customer  
> So that I can check if I want to order something  
> I would like to see a list of dishes with prices.
> 
> As a customer  
> So that I can order the meal I want  
> I would like to be able to select some number of several available dishes.
> 
> As a customer  
> So that I can verify that my order is correct  
> I would like to see an itemised receipt with a grand total.

Use the `twilio-python` package to implement this next one. You will need to use
mocks too.

> As a customer  
> So that I am reassured that my order will be delivered on time  
> I would like to receive a text such as "Thank you! Your order was placed and
> will be delivered before 18:52" after I have ordered.

#### request breakdown
> customer input:  
>> check - see a list - eventually order dishes   
>> list: dishes with prices.
>   
>> order picked dishes    
>> select some number of several available dishes    
>> list: filter dishes    
> 
>> verify that my order is correct   
>> see an itemised receipt with a grand total   
>> list: filtered items with prices and total   


> system output: 
>> So that I am reassured that my order will be delivered on time  
>> I would like to receive a text such as "Thank you! Your order was placed and
>> will be delivered before 18:52" after I have ordered.
>> string: message based on reasonable delivery time (e.g. ~30 min)

### design processing

intitializer:
    add resturants
    add dishes for each resturants
    nested dictionary
        app{
            resturant1
                {dishe1
                    {price, time}}
                    ....
            resturants2
                {dishe1
                    {price, time}}
                    ....
            ....
            }
list resturants
    >>select rest
list dishes
liste orders

### integration

```
>>> class TakeawayApp   (list resturants)
    > parameters:   none
    > properties:   1.list of resturnats - resturants
                    2.list of customers - customers
                    3.list of Orders - orders

        methods:    add
                    > parameters:   
                    > actions:      
                    > return:       
                    list_rest
                    > parameters:   
                    > actions:      
                    > return:       
                    select_rest
                    > parameters:   
                    > actions:      
                    > return:       
                    list_rest_with_dishes
                    > parameters:   
                    > actions:      
                    > return:       
                    confirm_order
                    > parameters:   
                    > actions:      
                    > return:       

    ----------------------------------------------

>>> class Resturant (main container of DishEntry)
    > parameters:   1.name of the resturant
    > properties:   1.list of dishes - dish_entries

        methods:    add_entry
                    > parameters:   1.class entry
                    > actions:      1. add dish
                    > return:       none
                    get_entries     
                    > parameters:   1.class entry
                    > actions:      1. retrive list of dishes
                    > return:       list

    ----------------------------------------------

>>> class DishEntry (single item with price and preparation time)
    > parameters:     1.name of the food  2.price   3.cooking time in minutes
    > properties:     1.2.3(same as 1.2.3 input)

        methods:    none

    ----------------------------------------------

>>> class Customer  (single item with distance from resturant)
    > parameters:   1.Name  2.Address
    > properties:   (same as above)

    ----------------------------------------------
>>> class Order
    > parameters:   1.order number  2.list of dishes
    > properties:   (same as above)

        methods:    checkout

    ----------------------------------------------
>>> class DeliveryService  (single service linked to order)
    > parameters:   
    > properties:   

        methods:    received

    ----------------------------------------------

```

### File signature
lib/resturants.py   tests/test_resturants.py
lib/

### Main code signature
>>> class TakeawayApp()
>>> class Resturant()
>>> class DishEntry()
>>> class Customer()
>>> class Order()
>>> class DeliveryService()

### Process
1. implementation of resturants and order entries in folder 01_mock_test_version
    copy of file are store in 

