
# Import modules and libraries in python

Previously, you explored libraries and modules. You learned that a module is a Python file that contains additional functions, variables, classes, and any kind of runnable code. You also learned that a library is a collection of modules that code users can access in their programs. You were introduced to a few modules in the Python Standard Library and a couple of external libraries. In this reading, you'll learn how to import a module that exists in the Python Standard Library and use its functions. You'll also expand your understanding of external libraries.

## The Python Standard Library

The Python Standard Library is an extensive collection of Python code that often comes packaged with Python. It includes a variety of modules, each with pre-built code centered around a particular type of task.

For example, you were previously introduced to the following modules in the Python Standard Library:

- The `re` module, which provides functions used for searching for patterns in log files
  <br>
- The `csv` module, which provides functions used when working with `.csv` files
  <br>
- The `glob` and `os` modules, which provide functions used when interacting with the command line
  <br>
- The `time` and `datetime` modules, which provide functions used when working with timestamps

Another Python Standard Library module is `statistics`. The `statistics` module includes functions used when calculating statistics related to numeric data. For example, `mean()` is a function in the `statistics` module that takes numeric data as input and calculates its mean (or average). Additionally, `median()` is a function in the `statistics` module that takes numeric data as input and calculates its median (or middle value).

## How to import modules from the Python Standard Library

To access modules from the Python Standard Library, you need to import them. You can choose to either import a full module or to only import specific functions from a module.

### Importing an entire module

To import an entire Python Standard Library module, you use the `import` keyword. The `import` keyword searches for a module or library in a system and adds it to the local Python environment. After `import`, specify the name of the module to import. For example, you can specify `import statistics` to import the `statistics` module. This will import all the functions inside of the `statistics` module for use later in your code.

As an example, you might want to use the `mean()` function from the `statistics` module to calculate the average number of failed login attempts per month for a particular user. In the following code block, the total number of failed login attempts for each of the twelve months is stored in a list called `monthly_failed_attempts`. The following code uses the `mean()` function to calculate the average of the monthly failed login attempts and stores the result in `mean_failed_attempts`.

```
import statistics
monthly_failed_attempts = [20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19]
mean_failed_attempts = statistics.mean(monthly_failed_attempts)
print("mean:", mean_failed_attempts)
```

It outputs:

`mean: 35.25`

The output returns a mean of `35.25`. You might notice the outlying value of `178` and want to find the middle value as well. To do this through the `median()` function, you can use the following code:

```
import statistics
monthly_failed_attempts = [20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19]
median_failed_attempts = statistics.median(monthly_failed_attempts)
print("median:", median_failed_attempts)
```

It outputs:

`median: 20.5`

This gives you the value of `20.5`, which might also be useful for analyzing the user's failed login attempt statistics.

> [!Note]
> When importing an entire Python Standard Library module, you need to identify the name of the module with the function when you call it. You can do this by placing the module name followed by a period (`.`) before the function name. For example, the previous code blocks use `statistics.mean()` and `statistics.median()` to call those functions.

### Importing specific functions from a module

To import a specific function from the Python Standard Library, you can use the `from` keyword. For example, if you want to import just the `median()` function from the `statistics` module, you can write from `statistics import median`.

To import multiple functions from a module, you can separate the functions you want to import with a comma. For instance, `from statistics import mean, median` imports both the `mean()` and the `median()` functions from the statistics module.

An important detail to note is that if you import specific functions from a module, you no longer have to specify the name of the module before those functions. You can examine this in the following code, which specifically imports only the `median()` and the `mean()` functions from the `statistics` module and performs the same calculations as the previous examples:

```
from statistics import mean, median
monthly_failed_attempts = [20, 17, 178, 33, 15, 21, 19, 29, 32, 15, 25, 19]
mean_failed_attempts = mean(monthly_failed_attempts)
print("mean:", mean_failed_attempts)
median_failed_attempts = median(monthly_failed_attempts)
print("median:", median_failed_attempts)
```

It outputs:

```
mean: 35.25
median: 20.5
```

It is no longer necessary to specify `statistics.mean()` or `statistics.median()` and instead the code incorporates these functions as `mean()` and `median()`.

## External libraries

In addition to the Python Standard Library, you can also download external libraries and incorporate them into your Python code. For example, previously you were introduced to Beautiful Soup (`bs4`) for parsing HTML files and NumPy (`numpy`) for arrays and mathematical computations. Before using them in a Jupyter Notebook or a Google Colab environment, you need to install them first.

To install a library, such as `numpy`, in either environment, you can run the following line prior to importing the library:

`%pip install numpy`

This installs the library so you can use it in your notebook.

After a library is installed, you can import it directly into Python using the `import` keyword in a similar way to how you used it to import modules from the Python Standard Library. For example, after the `numpy` install, you can use this code to import it:

`import numpy`