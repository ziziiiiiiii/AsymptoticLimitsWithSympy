# Takes input from the user in the form of asymptotic functions. The limit
# of these functions is found. Using the asymptotic symbol provided, the user
# is then returned an output of whether the relationship between the equations
# input is true.
from sympy import *

def asymptotic_analysis(left_func_str, right_func_str, asymptotic_symbol):
    # Validate asymptotic symbol
    if asymptotic_symbol not in {'O', 'Θ', 'Ω'}:
        raise ValueError("Invalid asymptotic symbol. Use 'O', 'Θ', or 'Ω'.")
    
    n = symbols('n', positive=True, real=True)
    
    # Replace 'lg' and 'ln' with 'log' for consistency
    left_func_str = left_func_str.replace('ln', 'log').replace('lg', 'log')
    right_func_str = right_func_str.replace('ln', 'log').replace('lg', 'log')
    
    # Parse the left and right functions using sympify for safer evaluation
    try:
        left_func = sympify(left_func_str, locals={'log': log, 'n': n, 'e': E, 'pi': pi, 'π': pi})
        right_func = sympify(right_func_str, locals={'log': log, 'n': n, 'e': E, 'pi': pi, 'π': pi})
    except Exception as e:
        raise ValueError(f"Invalid function expression: {e}")
    
    # Simplify the functions
    left_func = simplify(left_func)
    right_func = simplify(right_func)
    
    # Compute the limit of the ratio left_func / right_func as n -> oo
    if(left_func != 0) and (right_func != 0):
        ratio = left_func / right_func
        lim = limit(ratio, n, oo)
    elif (left_func == 0) and (right_func == 0):
        return True
    elif (left_func == 0):
        if (asymptotic_symbol == 'O'):
            return True
        elif (asymptotic_symbol == 'Θ'):
            return False
        elif (asymptotic_symbol == 'Ω'):
            return False
    elif (right_func == 0):
        if (asymptotic_symbol == 'O'):
            return False
        elif (asymptotic_symbol == 'Θ'):
            return False
        elif (asymptotic_symbol == 'Ω'):
            return True

    # Determine the result based on the asymptotic symbol
    if asymptotic_symbol == 'O':
        # For O, the limit should be finite (including zero)
        return lim.is_finite
    elif asymptotic_symbol == 'Θ':
        # For Θ, the limit should be a finite positive number
        return lim.is_finite and lim > 0
    elif asymptotic_symbol == 'Ω':
        # For Ω, the limit should be positive (including infinity)
        return lim > 0 or lim == oo
    else:
        # This should never be reached due to the initial validation
        raise ValueError("Invalid asymptotic symbol. Use 'O', 'Θ', or 'Ω'.")
    
# Example function calls:
# asymptotic_analysis("(log(n))^2", "lg(n^3)", "O")
# output: False

# asymptotic_analysis("2*n^2 + n*log(n) + 5", "n^2", "Θ")
# output: True

# asymptotic_analysis("n^2 + n + 5", "n*(log(n))^2", "Ω")
# output: True

# asymptotic_analysis("log(n)", "log(n)", "O")
# output: True

# asymptotic_analysis("log(n)", "log(n)", "Θ")
# output: True

# asymptotic_analysis("log(n)", "log(n)", "Ω")
# output: True

# asymptotic_analysis("log(n)", "1", "Ω")
# output: True

# asymptotic_analysis("log(n)", "1", "O")
# output: False

# asymptotic_analysis("n*log(n^2)", "n*log(n)", "Θ")
# output: True

# asymptotic_analysis("1/n","1","O")
# ouput: True

# asymptotic_analysis("1/n","1","Ω")
# output: False

# asymptotic_analysis("1/n","1","Θ")
# output: False