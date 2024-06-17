[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/gQ_doPhb)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15279876&assignment_repo_type=AssignmentRepo)
# APAi 5 Session 3 Assignment

# Int

# encoded_from_base10
This function returns a string encoding in the "base" for the the "number" using the "digit_map"
Conditions that this function must satisfy:
1. An error is raised ValueError if number is not in range 2 <= base <= 36 
2. invalid base ValueError must have relevant information
3. digit_map must have sufficient length to represent the base
4. must return proper encoding for all base ranges between 2 to 36 (including)
5. must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
6. the digit_map must not have any repeated character, else ValueError
7. the repeating character ValueError message must be relevant
8. you cannot use any in-built functions in the MATH module

# digit_map

An array containing all the possible digits in a particular base. For eg: For Base -2 , digit_map = [0,1], For Base -16 , digit_map=[0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F]

# ValueError
An Exception type raised to denote the value passed is not supported.

# Math
Python Module for doing math operations.

# isclose
Comparing floating numbers like 0.3(not stored in absolute terms) can be done using round method. The comparision can be done in relative terms or absolute terms , isclose function does that for us.

For very small numbers use absolute tolerance, For larger numbers use relative tolerance<br>
    Relative Tolerance - Percentage different allowed.<br>
    Absolute Tolerance - Ignore relative tolerance numbers are below the defined absolute tolerance<br> 
    eg: 
    
    x = 0.00000000000001
    
    y = 0.00000000000002
    
    isclose(x, y, rel_tol=0.01) # False
    
    isclose(x, y, rel_tol=0.01, abs_tol=0.01) # True


# Storing float numbers
Some numbers cannot be stored in absolute terms like eg: 3.999999999999999999999999999999, 0.3 as a result the floor operation might give different result
    - math.floor(3.9999999999999999999999999999999999999999) = 4
Also in such cases equality condition is not met. For eg: 0.3 = 0.1 + 0.1 + 0.1 will result in False

# Formula for Calculating Quotient and Remainder
1. Modulo(%) and Quotient(//) are complex operators and works weirdly.Follow the equation
    - a = b * (a//b) + (a%b)
2. a %b  behaves differently for positive and negative a and b
    - a = 13 , b = 4 , a % b = 1
    - a = -13 , b =4 , a %b = 3
    - a = 13 , b = -4 , a%b = -3 
    - a = -13 , b = -4 , a%b = -1 

# Base Conversion 
3. Hex to Decimal
    - FF = $15 * 16^1 + 15 * 16^0 = 255$
4. Decimal to Hex
    - 1500 in hex
        - (1)- Largest power = 162 = 256 <br>
        - (2)- 256 × 5 = 1280, so (5 × 162)
        - (3)-	1500 - 1280 = 220
        - (4)-	16 × 13 = 208, so (13 × 161)
        - (5)-	220 - 208 = 12
        - (6)-	16 is larger than 12, so 12 is the value in the 160 place value
        - (7)-	1500 = (5 × 162) + (13 × 161) + (12 × 160)
        - (8)-	Remember that 10-15 have letter numerals In hex: 13 = D, and 12 = C
        - (9)- Therefore the hex value of 1500 is: 5DC

# Fractions
Use of math.Fractions to to manage floating numbers. 

# Use of truncation , Floor and Ceil
Truncate and Floor and Ceil behave differently when dealing with negative numbers. Floor takes the number to the left(away from zero) and the ceil towards right(away from zero).
    - floor(10.3)  # 10
    - floor(-10.3) # -11
    - ceil(10.3) # 11
    - ceil(-10.3) # 10 
    - trunc(10.3) # 10
    - trunc(-10.3) # -10
# Round
1. Round
    - round(888.88, 1) #888.90
    - round(888.88, 0) #889.0
    - round(888.88, -1) # 890.0
    - round(888.88, -2) # 900.0
    - round(888.88, -3) # 1000.0
    - round(888.88, -4) # 0
    - round(-1.25, 1) # -1.25 #bankers rounding #HALF_ROUND_EVEN
    - round(-1.35, 1) # - 1.40 #bankers rounding #HALF_ROUND_EVEN
    - round(15, -1) # 20 #bankers rounding #HALF_ROUND_EVEN
    - round(25, -1) # 20 #bankers rounding #HALF_ROUND_EVEN

# Storing Decimal Numbers
1. Storing Decimals using math.Decimal is expensive in case of storing not actual numbers like 3.1415 unlike float 3.1415

# bin(x)
Convert the number in Base 2.

# hex(x)
Convert the number in Base 16.

