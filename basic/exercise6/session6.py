from functools import wraps

#q1
def check_docstring_len(min_length):
    def check_docstring(func):
        "Closure Function"
        @wraps(func) # to bring back all the normal fnc characteristics
        def inner():
            #Return function docstring
            return True if len(func.__doc__)>min_length else False
        
        # Return the wrapper function
        return inner
    return check_docstring

@check_docstring_len(50)
def fnc_docs():
    "Function Docstring characters should be greater than 50"
    pass

#q2
def next_fibonacci_closure():
    a, b = 0, 1
    
    def get_next():
        nonlocal a, b
        result = b
        a, b = b, a + b
        return result
    
    return get_next

#q3
# Global dictionary to store function call counts
function_call_counts = {
    'add': 0,
    'mul': 0,
    'div': 0
}

# Closure to count function calls and update the global dictionary
def count_function_calls(func):
    def inner(*args, **kwargs):
        # Update the global dictionary based on the function name
        function_name = func.__name__
        if function_name in function_call_counts:
            function_call_counts[function_name] += 1
        else:
            function_call_counts[function_name] = 1
        
        # Call the original function and return its result
        return func(*args, **kwargs)
    
    # Return the wrapper function
    return inner

# Sample functions to demonstrate usage
@count_function_calls
def add(a, b):
    return a + b

@count_function_calls
def mul(a, b):
    return a * b

@count_function_calls
def div(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero")

# # Example usage
# print(add(2, 3))  # Outputs: 5
# print(mul(4, 5))  # Outputs: 20
# print(div(10, 2)) # Outputs: 5.0

# # Printing the global dictionary after function calls
# print(function_call_counts)

#question-4

function_call_counts_add = {
    'add4': 0,
}
function_call_counts_mul = {
    'mul4': 0,
}
function_call_counts_div = {
    'div4': 0,
}

def count_function_calls_fact4(function_call_cnt):
    def count_function_calls4(func):
        def inner4(*args, **kwargs):
            # Update the global dictionary based on the function name
            function_name = func.__name__
            if function_name in function_call_cnt:
                function_call_cnt[function_name] += 1
            else:
                function_call_cnt[function_name] = 1

            # Call the original function and return its result
            return func(*args, **kwargs)

        # Return the wrapper function
        return inner4
    return count_function_calls4




@count_function_calls_fact4(function_call_counts_add)
def add4(a, b):
    return a + b

@count_function_calls_fact4(function_call_counts_mul)
def mul4(a, b):
    return a * b

@count_function_calls_fact4(function_call_counts_div)
def div4(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero")