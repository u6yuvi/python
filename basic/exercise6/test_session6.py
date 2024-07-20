import session6
from session6 import check_docstring_len
import pytest
import inspect
#q1

def test_session6_1_docstring_returns_bool():
    @check_docstring_len(50)
    def fnc_docs():
        "Function Docstring"
        pass
    assert isinstance(fnc_docs(),bool)

def test_session6_1_docstring_required_params():

    with pytest.raises(TypeError):
        @check_docstring_len()
        def fnc_docs():
            "Function Docstring"
            pass

def test_session6_1_docstring_len_gt_50():
    @check_docstring_len(50)
    def fnc_docs():
        "Function Docstring characters should be greater than 50"
        pass
    assert fnc_docs()==True

def test_session6_1_docstring_len_lt_50():
    @check_docstring_len(50)
    def fnc_docs():
        "Function Docstring"
        pass
    assert fnc_docs()==False

#q2
def test_session6_2_fibonnaci_ntimes():
    next_fib = session6.next_fibonacci_closure()
    for i in range(4):
        res = next_fib()
    assert res==3

def test_session6_2_initial_zero_fibonacci():
    next_fib = session6.next_fibonacci_closure()
    assert next_fib() == 1

def est_session6_2_consecutive_fibonacci_numbers():
    next_fib = session6.next_fibonacci_closure()
    
    for expected in [1, 1, 2, 3, 5, 8, 13, 21, 34]:
        assert next_fib() == expected

def test_session6_3_counter_add():
    #ensure global variable is 
    session6.function_call_counts = {}
    for i in range(10):
        session6.add(2,3)
    assert session6.function_call_counts["add"]==10, "Counter for add is not updated successfully"

def test_session6_3_counter_mul():
    session6.function_call_counts = {}
    for i in range(10):
        session6.mul(2,3)
    assert session6.function_call_counts["mul"]==10, "Counter for mul is not updated successfully"

def test_session6_3_counter_div():
    session6.function_call_counts = {}
    for i in range(10):
        session6.div(10,2)
    assert session6.function_call_counts["div"]==10, "Counter for div is not updated successfully"

def test_session6_3_counter_add_mul_div():
    session6.function_call_counts = {}
    for i in range(10):
        session6.add(2,3)
        session6.mul(2,3)
        session6.div(10,2)
    assert session6.function_call_counts["div"]==10, "Counter for div is not updated successfully"
    assert session6.function_call_counts["add"]==10, "Counter for add is not updated successfully"
    assert session6.function_call_counts["mul"]==10, "Counter for mul is not updated successfully"

def test_session6_3_counter_wrong_dict_key():
    session6.function_call_counts = {}
    with pytest.raises(KeyError):
        session6.div(10,2)
        assert session6.function_call_counts["div1"]==10

def test_session6_3_counter_wrong_func_name():
    session6.function_call_counts = {}
    with pytest.raises(AttributeError):
        session6.div1(10,2)


#q4
def test_session6_4_counter_add():
    assert session6.function_call_counts_add == {"add4":0}
    for i in range(10):
        session6.add4(2,3)
    assert session6.function_call_counts_add["add4"]==10, "Counter for add is not updated successfully"

def test_session6_4_counter_mul():
    assert session6.function_call_counts_mul == {"mul4":0}
    for i in range(10):
        session6.mul4(2,3)
    assert session6.function_call_counts_mul["mul4"]==10, "Counter for mul is not updated successfully"

def test_session6_4_counter_div():
    assert session6.function_call_counts_div == {"div4":0}
    for i in range(10):
        session6.div4(10,2)
    assert session6.function_call_counts_div["div4"]==10, "Counter for div is not updated successfully"


def test_session6_4_counter_add_mul_div():
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
    session6.function_call_counts_add = {}
    session6.function_call_counts_mul = {}
    session6.function_call_counts_div = {}
    with pytest.raises(KeyError):
        session6.div4(10,2)
        assert session6.function_call_counts_div["div1"]==10

def test_session6_4_counter_wrong_func_name():
    session6.function_call_counts = {}
    with pytest.raises(AttributeError):
        session6.div5(10,2)