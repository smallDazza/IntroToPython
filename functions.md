
## Functions:

- DRY : Dont repeat Yourself
- One of the best tools for following DRY

- blocks of code that performs a specific task
- Can be reused, also helps makes the program modular and manageable.
### Syntax:
~~~
    def function_name(parameters "optional"):
        # code blocks #
        return value
~~~
~~~
    Calling a function:
        function_name()
~~~

### Scope:
~~~
    - Children can access parents scope
    - but Parents cannot access childrens scope
~~~

## Return keywprd:
~~~
    - Returns a value from function
    - also immediately ends the function process
    - good practice to use return instead of 'print'.
~~~

## Arguments and Parameters:
    - Arguments are values to pass to a function.
    - Parameters are variables that allows us to pass to a function.
    - Positional arguments = are arguments in the correct positioning as the parameters.
    - Default arguments / optional parameters = paramters that assume value if a value is NOT provided. Eg sum(a, b=2). b value will equal 2 if no b argument value given.
    - Keyword arguments = assign a value to the arguments when calling function.
