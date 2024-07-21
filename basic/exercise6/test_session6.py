import session6
import os
from session6 import check_docstring_len
import pytest
import inspect
import re
print("A",os.getcwd())

def test_session6_readme_exists():
    """
    Test to check if Readme file exists
    """
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_session6_readme_500_words():
    """
    Test to check if Readme file has more than 500 words
    """
    readme_words=[word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_session5_readme_file_for_more_than_10_hashes():
    """
    Test if Redme has 10 headers
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_session5_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 



def test_session5_function_name_had_cap_letter():
    """ A. failures_message: You have used Capital letter(s) in your function names
        B. Once you write this test, that checks formatting by checking # being used more than 10 times, \
        it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_session6_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

############################## Assignment Validations###########################

def test_session6_1_docstring_returns_bool():
    """Check if the retuned value is of type bool
    """
    @check_docstring_len(50)
    def fnc_docs():
        "Function Docstring"
        pass
    assert isinstance(fnc_docs(),bool)

def test_session6_1_docstring_required_params():
    """
    Checks for the required parameter in the closure factory
    """

    with pytest.raises(TypeError):
        @check_docstring_len()
        def fnc_docs():
            "Function Docstring"
            pass

def test_session6_1_docstring_len_gt_50():
    """
    Checks for the docstring length to be greater than 50
    """
    @check_docstring_len(50)
    def fnc_docs():
        "Function Docstring characters should be greater than 50"
        pass
    assert fnc_docs()==True

def test_session6_1_docstring_len_lt_50():
    """
    Returns False for the docstring length less than than 50
    """
    @check_docstring_len(50)
    def fnc_docs():
        "Function Docstring"
        pass
    assert fnc_docs()==False

#q2
def test_session6_2_fibonnaci_ntimes():
    """
    Checkt the next fibonnaci value after n times
    """
    next_fib = session6.next_fibonacci_closure()
    for i in range(4):
        res = next_fib()
    assert res==3

def test_session6_2_initial_fibonacci_number():
    """
    Check the first fibonnaci number
    """
    next_fib = session6.next_fibonacci_closure()
    assert next_fib() == 1

def test_session6_2_consecutive_fibonacci_numbers():
    """Check fibbonnaci sequence for multiple positions
    """
    next_fib = session6.next_fibonacci_closure()
    
    for expected in [1, 1, 2, 3, 5, 8, 13, 21, 34]:
        assert next_fib() == expected

def test_session6_2_fibonnaci_arguments():
    """Check fibbonnaci sequence for argument
    """
    with pytest.raises(TypeError,match=r".*next_fibonacci_closure()*"):
        next_fib = session6.next_fibonacci_closure(2)
        for expected in [1, 1, 2, 3, 5, 8, 13, 21, 34]:
            assert next_fib() == expected


def test_session6_3_counter_add():
    """
    Check add increments
    """
    #ensure global variable is 
    session6.function_call_counts = {}
    for i in range(10):
        session6.add(2,3)
    assert session6.function_call_counts["add"]==10, "Counter for add is not updated successfully"

def test_session6_3_counter_mul():
    """
    Check mul increment
    """
    session6.function_call_counts = {}
    for i in range(10):
        session6.mul(2,3)
    assert session6.function_call_counts["mul"]==10, "Counter for mul is not updated successfully"

def test_session6_3_counter_div():
    """
    Check div increment
    """
    session6.function_call_counts = {}
    for i in range(10):
        session6.div(10,2)
    assert session6.function_call_counts["div"]==10, "Counter for div is not updated successfully"

def test_session6_3_counter_add_mul_div():
    """
    Check add, mul ,div increment
    """
    session6.function_call_counts = {}
    for i in range(10):
        session6.add(2,3)
        session6.mul(2,3)
        session6.div(10,2)
    assert session6.function_call_counts["div"]==10, "Counter for div is not updated successfully"
    assert session6.function_call_counts["add"]==10, "Counter for add is not updated successfully"
    assert session6.function_call_counts["mul"]==10, "Counter for mul is not updated successfully"

def test_session6_3_counter_wrong_dict_key():
    """
    Check wrong dict key name
    """
    session6.function_call_counts = {}
    with pytest.raises(KeyError):
        session6.div(10,2)
        assert session6.function_call_counts["div1"]==10

def test_session6_3_counter_wrong_func_name():
    """
    Check wrong funct name 
    """
    session6.function_call_counts = {}
    with pytest.raises(AttributeError):
        session6.div1(10,2)

def test_session6_3_div_by_0():
    """
    Check wrong funct name 
    """
    session6.function_call_counts = {}
    with pytest.raises(ValueError,match=r"Division by zero"):
        session6.div(10,0)

def test_session6_3_add_wrong_inputtype():
    """
    Check for wrong input type to add fnc
    """
    session6.function_call_counts = {}
    with pytest.raises(TypeError,match=r"Value of a and b should*"):
        session6.add(10,"abc")

def test_session6_3_mul_wrong_inputtype():
    """
    Check for wrong input type to mul fnc
    """
    session6.function_call_counts = {}
    with pytest.raises(TypeError,match=r"Value of a and b should*"):
        session6.mul(10,"abc")

def test_session6_3_div_wrong_inputtype():
    """
    Check for wrong input type to mul fnc
    """
    session6.function_call_counts = {}
    with pytest.raises(TypeError,match=r"Wrong input type for b*"):
        session6.div(10,"abc")

def test_session6_3_div_wrong_inputtype():
    """
    Check for wrong input type to mul fnc
    """
    session6.function_call_counts = {}
    with pytest.raises(TypeError,match=r"Wrong input type for a*"):
        session6.div("abc",10)

#q4
def test_session6_4_counter_add():
    """
     Check add increments
    """
    assert session6.function_call_counts_add == {"add4":0}
    for i in range(10):
        session6.add4(2,3)
    assert session6.function_call_counts_add["add4"]==10, "Counter for add is not updated successfully"

def test_session6_4_counter_mul():
    """
     Check mul increments
    """
    assert session6.function_call_counts_mul == {"mul4":0}
    for i in range(10):
        session6.mul4(2,3)
    assert session6.function_call_counts_mul["mul4"]==10, "Counter for mul is not updated successfully"

def test_session6_4_counter_div():
    """
     Check div increments
    """
    assert session6.function_call_counts_div == {"div4":0}
    for i in range(10):
        session6.div4(10,2)
    assert session6.function_call_counts_div["div4"]==10, "Counter for div is not updated successfully"


def test_session6_4_counter_add_mul_div():
    """
     Check add mul, div increments
    """
    assert session6.function_call_counts_add == {"add4":10}
    session6.add4(2, 3)
    assert session6.function_call_counts_add == {'add4': 11}

    assert session6.function_call_counts_mul == {"mul4":10}
    session6.mul4(2, 3)
    assert session6.function_call_counts_mul == {'mul4': 11}

    assert session6.function_call_counts_div == {"div4":10}
    session6.div4(2, 3)
    assert session6.function_call_counts_div == {'div4': 11}

def test_session6_4_counter_wrong_dict_key():
    """
    Check wrong dict keys
    """
    session6.function_call_counts_add = {}
    session6.function_call_counts_mul = {}
    session6.function_call_counts_div = {}
    with pytest.raises(KeyError):
        session6.div4(10,2)
        assert session6.function_call_counts_div["div1"]==10

def test_session6_4_counter_wrong_func_name():
    """
    Check wrong funct name 
    """
    session6.function_call_counts = {}
    with pytest.raises(AttributeError):
        session6.div5(10,2)

def test_session6_4_div_by_0():
    """
    Check wrong funct name 
    """
    session6.function_call_counts = {}
    with pytest.raises(ValueError,match=r"Division by zero"):
        session6.div4(10,0)


def test_session6_4_add_wrong_inputtype():
    """
    Check for wrong input type to add fnc
    """
    session6.function_call_counts = {}
    with pytest.raises(TypeError,match=r"Value of a and b should*"):
        session6.add4(10,"abc")

def test_session6_4_mul_wrong_inputtype():
    """
    Check for wrong input type to mul fnc
    """
    session6.function_call_counts = {}
    with pytest.raises(TypeError,match=r"Value of a and b should*"):
        session6.mul4(10,"abc")

def test_session6_4_div_wrong_inputtype():
    """
    Check for wrong input type to mul fnc
    """
    session6.function_call_counts = {}
    with pytest.raises(TypeError,match=r"Wrong input type for b*"):
        session6.div4(10,"abc")

def test_session6_4_div_wrong_inputtype():
    """
    Check for wrong input type to mul fnc
    """
    session6.function_call_counts = {}
    with pytest.raises(TypeError,match=r"Wrong input type for a*"):
        session6.div4("abc",10)
