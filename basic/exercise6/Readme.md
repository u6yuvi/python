# Questions
1. Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable (+ 4 tests) - 200
2. Write a closure that gives you the next Fibonacci number (+ 2 tests) - 100
3. We wrote a closure that counts how many times a function was called. Write a new one that can keep track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts 
4. Modify above such that now we can pass in different dictionary variables to update different dictionaries


# check_docstring_len

Closure factory that takes in the parameter to be passed to the closure. The closure function takes a function and then check whether the function passed has a docstring with more than 50 characters.
We use @wrap which is a decorator that is applied to the wrapper function of a decorator. It updates the wrapper function to look like wrapped function by copying attributes such as __name__, __doc__ (the docstring), etc.This allows us to access the attributes and write conditions on them.On such condition od docstring has been implemented in this closure function.
## Following tests has been added as part of unit test to the above function:
1. Check if the retuned value is of type bool
2. Checks for the required parameter in the closure factory
3. Checks for the docstring length to be greater than 50
4. Returns False for the docstring length less than than 50

# next_fibonacci_closure
This function initializes the variables a and b which will store the last two Fibonacci numbers.
Inner Function get_next:

This inner function get_next() is a closure that captures the variables a and b from the enclosing scope.
It updates a and b to generate the next Fibonacci number sequence.
It returns result, which is the next Fibonacci number.
Return Statement:
The outer function next_fibonacci_closure returns the inner function get_next, which retains access to a and b across multiple calls.

The closure next_fib remembers the state of a and b between calls.
Each call to next_fib() returns the next Fibonacci number in the sequence.

## Unit Tests
1. Checkt the next fibonnaci value after n times
2. Check the first fibonnaci number
3. Check fibbonnaci sequence for multiple positions
4. Check fibbonnaci sequence for argument

# count_function_calls
Closure function that keeps track of how many times specific functions (add, mul, div) are called and updates a global dictionary variable with the counts
Global Dictionary `function_call_counts`:

This dictionary `function_call_counts` stores the counts of how many times each function (add, mul, div) has been called.
`count_function_calls` Function:

This function returns a closure `count_function_calls` that tracks the calls to any function it decorates.
track_function_calls_closure Closure:

This closure wraps around each function (add, mul, div) and increments the count in `function_call_counts` each time the function is called.
It uses `func.__name__` to dynamically retrieve the name of the function being called.
Decorated Functions (add, mul, div):

Each function is decorated with `@count_function_calls()` to enable tracking of their calls.

## Example Usage:
Calls to `add`, `mul`, and `div` demonstrate how the tracking mechanism works.

## Unit Tests added:
1. Check add increments
2. Check mul increment
3. Check div increment
4. Check add, mul, div increment
5. Check wrong dict key name
6. Check wrong funct name 

#  count_function_calls_fact4 
Closure function that can update different dictionary variables based on the context provided, we'll make a slight adjustment to the count_function_calls() function. This adjustment will allow us to pass in a custom dictionary to update when tracking function calls. Here's how you can implement it:

count_function_calls Function Modification:

The function count_function_calls_fact4(custom_dict) now accepts a custom_dict parameter. This dictionary is passed by the user to specify where the function call counts should be updated.
count_function_calls4 Closure:

This closure wraps around each function (add, mul, div) and increments the call count for the function's name (func.__name__) in the custom_dict provided by the user.
Decorated Functions (add, mul, div):

Each function is decorated with @count_function_calls_fact4(dict1) or @count_function_calls_fact4(dict2) to specify which dictionary (dict1 or dict2) should track its calls.

## Unit Tests
1. Check add increments
2. Check mul increment
3. Check div increment
4. Check add, mul, div increment
5. Check wrong dict key name
6. Check wrong funct name

