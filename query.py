"""
a)............List Vs Dictionary..........

List......

1.list stores multiple items in a single variable.
2.A list is created using square brackets [].
3.list items are accessed using an index.
4.a list can contain duplicate items.
5.ex:
    fruits=["mango","banana","apple"]

Dictionary......

1.A dictionary stores data in key-value pair.
2.a dictionary is created using curly braces {}.
3.Values are accessed using keys.
4.dictionary keys must be unique.
5.Ex:
    students={"name":"Fatema","age":21}


    
b).........*args vs **kwargs.......

*args......
*args allows a function to accept any number of positional arguments.
The arguments are stored in a tuple.

Ex:
 def add(*args):
     total=0
     for num in args:
         total+=num
     print("SUM: ",total)

add(10,20)
add(10,20,30)

1.accepts positional arguments.
2.stores arguments in a tuple.
3.it uses a single asterisk(*).
4.argument are passed without parameters name.
5.access value using loop or index.


**kwargs.......

**kwargs allows a function to accept any number of keyword arguments.
These arguments are stored in a dictionary.

Ex:
def student(**kwargs):
    for key,value in kwargs.items():
    print(key,":",value)

student(name="Fat",age=21,department="IIT")

1.accepts keyword arguments.
2.stores arguments in dictionary.
3.it uses a double asterisk(**).
4.it is useful when the number of named values is unknown.
5.access value using keys or loop.




"""
