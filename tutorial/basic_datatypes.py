import marimo

__generated_with = "0.14.12"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    # from helpers import run_tests
    # import inspect
    return mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Basic datatypes in Python""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # References

    Additional material can be found in the following references:

    * Official documentation on [Python build-in data types](https://docs.python.org/3/library/stdtypes.html)
    * Official documentation on [Python data model](https://docs.python.org/3/reference/datamodel.html)
    * Python For Everybody: [Variables, Expressions, and Statements](https://www.py4e.com/lessons/memory)
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Introduction
    In Python, we distinguish built-in data types and structures, which are more complex ways to organise and store data collections.
    In this tutorial we will cover the most commonly used ones.

    ## Built-in data types

    There are several built-in data types in Python.
    The most commonly used ones are the following:
      1. Integers (`int`), e.g.
      ```python
      1, -2, 0, 100
      ```
      2. Floats (`float`), e.g.
      ```python
      1.0, -2.5, 0.0, 100.0
      ```
      3. Strings (`str`), e.g.
      ```python
      "Hello, World", "1", "2.5"
      ```
      4. Booleans (`bool`), e.g.
      ```python
      True, False
      ```
      5. NoneType (`NoneType`), e.g.
      ```python
      None
      ```
    The built-in data types are the basic building blocks for representing and manipulating data.

    ## Data structures
    Data structures are more complex ways of organizing and storing data collections.
    Data structures may contain built-in data types as well as other data structures.
    The most commonly used data structures are:
      1. Lists (`list`), e.g.
      ```python
      [1, 2, 3], ["Hello", "World"], [1, 2.5, "Hello"]
      ```
      2. Tuples (`tuple`), e.g.
      ```python
      (1, 2, 3), ("Hello", "World"), (1, 2.5, "Hello")
      ```
      3. Dictionaries (`dict`), e.g.
      ```python
      {"key1": 1, "key2": 2}, {"key1": "Hello", "key2": "World"}, {"key1": 1, "key2": 2.5, "key3": "Hello"}
      ```
      4. Sets (`set`), e.g.
      ```python
      {1, 2, 3}, {"Hello", "World"}, {1, 2.5, "Hello"}
      ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Dynamic typing and `type()` function

    Python is a dynamically typed language.
    Dynamic typing means that the variable type is determined at runtime rather than being explicitly declared by the programmer.
    The type of a variable is determined by the value assigned to it.
    In Python, the type of a variable can be checked by the `type()` function.
    Let's see how this works in practice.
    """
    )
    return


@app.cell
def _():
    _a = 1
    print(f"My type is {type(_a)}")
    _a = 1.0
    print(f"My type has changed, now it is {type(_a)}")
    _a = "now I am a string"
    print(f"My type ha changed again, now it is {type(_a)}")
    _a = [1, 2, 3]
    print(f"I became a list now: {type(_a)}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    /// details | Note
        type: info

    Python is a **dynamically typed** language. The type of a variable is determined at runtime.
    ///
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    There is, however, a way to explicitly declare the type of a variable.
    This is useful for error checking, documentation, and code readability.
    Static typing, however, is optional in Python.
    Moreover, variables declared with static typing are not checked at runtime and can be reassigned to a different type.
    To prevent this from happening it is suggested to use external tools like [mypy](http://mypy-lang.org/) to check your code for type errors.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Arithmetics of built-in data types""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Arithmetic operations with integers

    In Python, the basic arithmetic operations are supported for integers.
    The following list shows the supported arithmetic operations and their corresponding symbols:

      * Addition: `+` (sum of two integers is an integer)
      * Subtraction: `-` (difference of two integers is an integer)
      * Multiplication: `*` (product of two integers is an integer)
      * Division: `/` (quotient of two integers is a float)
      * Floor division: `//` (quotient of two integers is an integer)
      * Modulo: `%` (remainder of two integers is an integer)
      * Exponentiation: `**`  (exponentiation of two integers is an integer)

    Let's see how these operations work in practice:
    """
    )
    return


@app.cell
def _():
    _x = 5
    _y = 3
    print(f"Addition: {_x + _y}")
    print(f"Subtraction: {_x - _y}")
    print(f"Multiplication: {_x * _y}")
    print(f"Division: {_x / _y}")
    print(f"Floor division: {_x // _y}")
    print(f"Exponentiation: {_x**_y}")
    print(f"Modulo: {_x % _y}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""Let's have a closer look at the difference between "standard" and floor division."""
    )
    return


@app.cell
def _():
    _x = 5
    _y = 3
    div = _x / _y
    floor_div = _x // _y
    print(f"Division: {div}, {type(div)}")
    print(f"Floor division: {floor_div}, {type(floor_div)}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    <div class="alert alert-block alert-info">
    <b>Remember:</b> The division operation <code>/</code> always returns a <code>float</code>.
    If you want the division to return <code>int</code>, you have to use the <code>//</code> operator.
    </div>
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Arithmetic operations with floats

    Floats share the same arithmetic operations as integers, with the difference that the result of such an operation is always a float.
    Let's see how these operations work in practice:
    """
    )
    return


@app.cell
def _():
    _x = 5.0
    _y = -2.0
    print(f"Addition: {_x + _y}")
    print(f"Subtraction: {_x - _y}")
    print(f"Multiplication: {_x * _y}")
    print(f"Division: {_x / _y}")
    print(f"Floor division: {_x // _y}")
    print(f"Exponentiation: {_x**_y}")
    print(f"Modulo: {_x % _y}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    <div class="alert alert-block alert-info">
    <b>Note:</b> The floor division operator <code>//</code> performs division and returns the largest integer less than or equal to the result.
    When operating on floats, it returns a float result, like -3.0 in the example above. When operating on integers, it returns an integer result.
    </div>
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Exercises on basic data type arithmetics""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    In the cell below you should write the code that solves the following exercises:

      1. Write a Python program to that gets three float numbers and retuns $(a + b) * c$.
      2. Write a Python program that computes the area of a circle with radius $r$. Use `math.pi` from the math library as the value of pi.
      2. Write a Python program that returns the solutions of the quadratic equation $ax^2 + bx + c = 0$. We consider only the case when there are two distinct solutions and both are real numbers.
    """
    )
    return


@app.function
def solution_addition_multiplication(a: float, b: float, c: float) -> float:
    """Adds a and b, then multiplies the result by c

    Args:
        a : first number
        b : second number
        c : third number

    Returns:
        - The result of the calculation
    """
    return


# @app.cell
# def _(mo):
#     button = mo.ui.run_button(label="Run tests")
#     button
#     return (button,)


# @app.cell
# def _(button, run_tests):
#     if button.value:
#         print(run_tests("basic_datatypes", "addition_multiplication"))
#     return


# @app.cell
# def _():
#     return


if __name__ == "__main__":
    app.run()
