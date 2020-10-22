# Short Functions

## Bank Interest

Let _p_ be a bank’s interest rate in percent per year. An initial amount _A_ has then grown to

<p align="center"><i>A</i> (1 + <i>p</i> / 100)<sup><i>n</i></sup></p>

after _n_ years. Make a function `interest` taking arguments _A_, _p_, and _n_, for computing the amount of money after several years and use it to compute how much money 1000 euros have grown to after three years with 5% interest rate.


## Temperature

The formula for converting Fahrenheit degrees to Celsius reads

<p align="center"><i>C</i> = <sup>5</sup>⁄<sub>9</sub> (<i>F</i> − 32)</p>

Write a function ``celsius(farenheit)`` that implements this formula.


## Dollars

Write a function `convert_to_usd`, which takes parameter `pln`, for an amount in PLN. The function should return the amount in USD. Assume 3.85 PLN = 1 USD.


## Net

Write a fucntion `calc_net`, which takes arguments:

* `gross` for gross price,
* `vat`, for VAT percentage (a number in a range 0–100). Default value for VAT should be 23%.

The function should return the net price. Think about the calculations you need to do.


## Short words

Write a function `get_short_words`, which takes a text and returns the list of words shorter than _n_ characters. _n_ is a function argument with a default value of 5.

### Example

```python
words = "To be or not to be this is a question".split(' ')

print(get_short_words(words))
print(get_short_words(words, 3))
```

Result:

```
['To', 'be', 'or', 'not', 'to', 'be', 'this', 'is', 'a']
['To', 'be', 'or', 'to', 'be', 'is', 'a']
```


### Additional task
Check in the Python documentation what a string method `split` does (see the example above).


## Initials

Write a functions `initials`, which takes a person's full name as an argument and converts all
the names but the last one into initials. Only the names beginning with capital letter should
be shortened.

### Example

```python
print(initials("Edgar Alan Poe"))
print(initials("Donatien Alphonse François de Sade"))
```

Result:

```
E. A. Poe
D. A. F. de Sade
```


## Movies

Write a function `message`, which takes as an argument a dictionary with the keys:

* **name**,
* **role**,
* **movie**.

The function should return a formatted string "In _movie_, _name_ is a _role_.", where _movie_, _name_, and _role_ is replaced with the corresponding values from the dictionary. If any of the values is missing from the dictionary, the function should return `None`.

### Example 1

```python
han = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

print(message(han))
```

Result:

```
In Star Wars, Han Solo is a smuggler.
```


### Example 2

```python
bilbo = {
    "name": "Bilbo Baggins",
    "role": "burglar"
}

print(message(bilbo))
```

Result:

```
None
```


## Quadratic Equation

Write a function `quadratic_equation(a, b, c)` that finds all **real** solutions of the quadratic equation of the form

```
a x² + b x + c = 0
```

The function should return a tuple containing zero, one, or two solutions. The tuple must be empty if either no solution exists or there is an infinite number of solutions.

You must correctly handle a case of _a_ equal to 0.


## Dice

Write a function `dice(num)`, which simulates a roll with a 6-side dice. `num` is a number of dice to throw. The function should return the sum of the dice.


## Two dice

Using the function `dice(num)` from the previous exercise, write a function `print_histogram(throws)` that rolls two dice _throws_ times and **prints** a histogram of the resulting numbers according to the example below:

```
 2: ##############
 3: #########################
 4: ##############################################
 5: #####################################################################
 6: ##################################################################
 7: ###########################################################################################
 8: ####################################################################
 9: ###################################################
10: ###################################
11: ##################
12: #################
```

Please mind the formatting (e.g. every number **must** span two characters and be right-aligned)!
