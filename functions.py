# coding: utf-8

def interest(A, n, p):
    """
    Let _p_ be a bank’s interest rate in percent per year. An initial amount _A_ has then grown to

                             n
        A = A ( 1 + p / 100 )

    after _n_ years. Make a function `interest` taking arguments _A_, _p_, and _n_, for computing
    the amount of money after several years and use it to compute how much money 1000 euros have
    grown to after three years with 5% interest rate.

    """
    # Write your code here


def celsius(farenheit):
    """
    The formula for converting Fahrenheit degrees to Celsius reads

        C = 5/9 (F − 32).

    Write a function ``celsius(farenheit)`` that implements this formula.
    """
    # Write your code here


def convert_to_usd(pln):
    """
    Write a function `convert_to_usd`, which takes parameter `pln`, for an amount in PLN.
    The function should return the amount in USD. Assume 3.85 PLN = 1 USD.
    """
    # Write your code here


def calc_net(gross, vat=23):
    """
    Write a fucntion `calc_net`, which takes arguments:

    * `gross` for gross price,
    * `vat`, for VAT percentage (a number in a range 0–100). Default value for VAT should be 23%.

    The function should return the net price. Think about the calculations you need to do.
    """
    # Write your code here


def get_short_words(text, n=5):
    """
    Write a function `get_short_words`, which takes a text and returns the list of words shorter
    than _n_ characters. _n_ is a function argument with a default value of 5.
    """
    # Write your code here


def initials(name):
    """
    Write a functions `initials`, which takes a person's full name as an argument and converts all
    the names but the last one into initials. Only the names beginning with capital letter should
    be shortened.
    """


def message(data):
    """
    Write a function `message`, which takes as an argument a dictionary with the keys:

    * **name**,
    * **role**,
    * **movie**.

    The function should return a formatted string "In _movie_, _name_ is a _role_.", where
    _movie_, _name_, and _role_ is replaced with the corresponding values from the dictionary.
    If any of the values is missing from the dictionary, the function should return `None`.
    """
    # Write your code here


def quadratic_equation(a, b, c):
    """
    Write a function `quadratic_equation(a, b, c)` that finds all **real** solutions of the quadratic equation of the form

        a x² + b x + c = 0

    The function should return a tuple containing zero, one, or two solutions. The tuple must be empty if either
    no solution exists or there is an infinite number of solutions.

    You must correctly handle a case of _a_ equal to 0.
    """
    # Write your code here


def dice(num):
    """
    Write a function `dice(num)`, which simulates a roll with a 6-side dice. `num` is a number
    of dice to throw. The function should return the sum of the dice.
    """
    # Write your code here


def histogram(throws=500):
    """
    Using the function `dice(num)` from the previous exercise, write a function `print_histogram(throws)` that
    rolls two dice _throws_ times and **prints** a histogram of the resulting numbers according to the example below:

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

    Please mind the formatting (e.g. every number **must** span two characters and be right-aligned)!
    """
    # Write your code here
