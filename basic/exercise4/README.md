# Qualean Class

Qualean class that is inspired by Boolean+Quantum concepts. We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. The moment you assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1) multiplies with it, and stores that number internally after using Banker rounding to the 10th decimal place. To understand this further.. imagine picking 100 times any number from 1, 0 or -1. You want to store this list. But before you can store it, the quantum nature of this class is going to pick another number (random.uniform(-1, 1)) and multiply it with the number you want to store. So if I wanted to store 1, 0, 1, -1, -1.. it might get stored as 0.00123123, 0, -0.123123, 0.63463, -0.36343. 
It implements these functions (with exactly the same names):

# and
Implements a method that returns bool expression of the `AND` operation between the class attribute(self.value) and the user input(q2)
In case, user input in None , it returns False

# or
Implements a method that returns bool expression of `OR` operation between the class attribute(self.value) and the user input(q2)
In case, user input in None , it returns False

# repr
Returns a string that represents information of the class.

# str
Returns a string that represents Qualean string it created.

# add 
Returns sum of the Qualean class attribute value  and the user given value afte rounding the sum upto 10 decimal places.
Currently supported Isntance type for User given value are of type float and Qualean.

# eq
Checks equality of the Qualean class attribute value  and the user given value.
Currently supported Isntance type for User given value are of type Qualean.Any other instance type raises TypeError.

# float
Returns the Qualean class attribute value 

# ge
Checks greater than and equal to condition  of the Qualean class attribute value  and the user given value 

Currently supported Isntance type for User given value are of type float and Qualean.Any other instance type raises TypeError.

# gt
Checks greater than  condition  of the Qualean class attribute value  and the user given value 

Currently supported Isntance type for User given value are of type float and Qualean.Any other instance type raises TypeError.

# invertsign
Retuns the negative value of the Qualean class attribute after rounding it to 10 decimal places.

# le

Checks less than and equal to condition  of the Qualean class attribute value  and the user given value after rounding Qualean class attribute to the 10 decimal places.

Currently supported Isntance type for User given value are of type float and Qualean.Any other instance type raises TypeError.

# lt
Checks less than condition  of the Qualean class attribute value  and the user given value after rounding Qualean class attribute to the 10 decimal places.

Currently supported Isntance type for User given value are of type float and Qualean.Any other instance type raises TypeError.

# mul
Returns product of the Qualean class attribute value  and the user given value after rounding Qualean class attribute to the 10 decimal places.

Currently supported Isntance type for User given value are of type float and Qualean.Any other instance type raises TypeError.

# sqrt
If Qualean class atrribute is greater than 0, returns square root value of the Qualean class atrribute after rounding the value to the 10 decimal places.
If value is less than 0, returns string value of the square root value of the Qualean class atrribute after rounding the value to the 10 decimal places.

# bool
Return truthiness of the Qualean class attribute

# init
Used to initialize objects of a class. It is also called a constructor. For Qualean class, it initialiaze the value from a uniform distribution between (-1,1) ,if the value is not passed.in case the value is passed