# Functions Used

Below are some of the python objects defined in the session_2.py file which is used in the testing_seesion_2.py file.

'Something',
'SomethingNew',
'add_something',
'clear_memory',
'critical_function',
'compare_strings_old',
'compare_strings_new',
'sleep',
'char_list',
'collection',
'__init__'

# Something

A python class with an attribute something_new with default value None.
Use of __repr__ function to describe the usage of the Class Something.
__init__(self) - self points to the pointer of the instantiated object of the class.

# SomethingNew

A python class with attributes i of type integer something of type Something
Use of __repr__ function to describe the usage of the Class SomethingNew. 

# Add_something 
Use this method to store something
reserved_Function - Abstract function , can be used to impelement new functionality.

# clear_memory
Method to clean the container containing something.Usage of garbage collection in this method keeps the memory peak lower. Although python's garbage collection is used, there is no harm to explicitly call it when working on constrained environment under low compute resources.

# critical_function:
Method that collects all the numbers between 1 and 1024*1024 and then deletes it. We also added garbage collection  for the deleted collection to ensure the memory is cleared as part of this function call itself rather than waiting for the garbage collection to do its task.
# compare_strings_old

Takes two string values and checks if the two string values are same and checks for character d in the character list of string a.

# compare_strings_new

Takes two string values and checks if the two string values are same and checks for character d in the character list of string a.

This is the optimised function using python intern where a user defined string object is made singleton so that every reference to the object is pointer to a single memory location and ensure no duplicate copies are created.
Although, python has its own intern methodology but uses certain rules(following python naming convention in a string only) to intern any object. 

Also to ensure faster processing of the function, we replaced usage of list with set which creats hashes for each element in the collection so that when we query the element in the collection, we donot iterate over the whole collection rather the lookup happens in O(1) using hashes. This speeds up the inference speed and is a good optimisation to ne included wherever possible.

# sleep
Function to halt the program for certain time

# char_list

List of all characters present in a string. The string characters are stored in the list.

# collection
List containing something objects

# __init__
Pointer to the address of the class object.

# Takeaways

1. Use of set over list if searching for elements in a collection.
2. Usage of garbage collection when deleting elements to keep check on peak memory.
3. Add __repr__ to add description about the Class usage.
4. Use of lower_case letter when using function name.
5. Use of `` sys.intern `` to enable python intern within the function.Refer ``compare_strings_new`` for example and usage.

