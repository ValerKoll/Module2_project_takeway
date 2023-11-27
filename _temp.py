class Data():
    resturants_data = {
        "Kung-Po Chinese":12,
        "Random Turkey":34,
        "Pizza Express Italian":67
        }

class ttt():
    def __init__(self, name, age):
        self. name = name
        self.age = age
        

list1 = []
for name, age in Data.resturants_data.items():
    list1.append(ttt(name, age))
    
print(list1[1].name)
b = list(filter(lambda i : i.name == 'Random Turkey', list1))
print(b[0].age)

    

