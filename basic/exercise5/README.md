Write a function that gives out the average run time per call, such that its definition is:

For eg:
def time_it(fn, *args, repetitons= 1, **kwargs): your code comes here.

We should be able to call it like this:

time_it(print, 1, 2, 3, sep='-', end= ' ***\n'. repetitons=5)
time_it(squared_power_list, 2, start=0, end=5, repetitons=5) #2 is the number you are calculating power of, [1, 2, 4, 8, 16, 32]
time_it(polygon_area, 15, sides = 3, repetitons=10) # 15 is the side length. This polygon supports area calculations of upto a hexagon
time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100) # 100 is the base temperature given to be converted
time_it(speed_converter, 100, dist='km', time='min', repetitons=200) #dist can be km/m/ft/yrd, time can be ms/s/m/hr/day, speed given by the user is in kmph

# time_it
This is a genralized function to call any function  user specified number of times and return the averagetime taken for calls

## time_it(fn, *args, repetitions= 1, **kwargs)
Function contains positional argments(fn,*args), keyword arguments(repetition,**kwargs)
Following checks are done in the function:
1. required positional argument
2. function definition
3. Arguments for function

# squared_power_list
Retuns list by raising number to power from start to end number. Default start is 0 and end is 5
eg:
squared_power_list(1,start=1, end=5) == [1,1,1,1]
squared_power_list(2,start=1, end=4) == [2,4,8]

Following checks are done in the function:
1. No of positional arguments
2. No of  keyword/named arguments
3. Instance type of postional arguments
4. Value of positional arguments
5. Value of keyword arguments
6. Instance type of postional arguments

# polygon_area
Retruns area of a regular polygon with number of sides between 3 to 6 bith inclusive
eg:
polygon_area(length, sides=3)
polygon_area(length, sides=4)
polygon_area(length, sides=5)
Following checks are done in the function:
1. No of positional arguments
2. No of  keyword/named arguments
3. Instance type of postional arguments
4. Value of positional arguments
5. Value of keyword arguments
6. Instance type of postional arguments

# temp_converter
Converts temprature from celsius 'c' to fahrenheit 'f' or fahrenheit to celsius
Retruns area of a regular polygon with number of sides between 3 to 6 bith inclusive
eg: 
temp_converter(25,temp_given_in='c') == 77.0
temp_converter(-25,temp_given_in='C') == -13.0
temp_converter(77,temp_given_in='f') == 25.0
temp_converter(-13,temp_given_in='F')

Following checks are done in the function:
1. No of positional arguments
2. No of  keyword/named arguments
3. Instance type of postional arguments
4. Value of positional arguments
5. Value of keyword arguments
6. Instance type of postional arguments

# speed_converter
Converts speed from kmph (provided by user as input) to different units dist can be km/m/ft/yrd time can be ms/s/min/hr/day 
Retruns area of a regular polygon with number of sides between 3 to 6 bith inclusive
eg:
speed_converter(36000,dist='KM',time='MS') == 0
speed_converter(36000,dist='KM',time='S') == 10
speed_converter(6000,dist='KM',time='MIN') == 100
speed_converter(100,dist='KM',time='HR') == 100 
speed_converter(100,dist='KM',time='DAY') == 2400

Maintains a dist mapping and time mapping which converts km to ft,m,yard and hour to ms,s,min,hr,day
Following checks are done in the function:
1. No of positional arguments
2. No of  keyword/named arguments
3. Instance type of keyword arguments
4. Value of positional arguments
5. Value of keyword arguments
6. Instance type of postional arguments

