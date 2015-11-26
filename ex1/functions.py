# Copyright (c) 2015,Vienna University of Technology,
# Department of Geodesy and Geoinformation
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Vienna University of Technology,
#      Department of Geodesy and Geoinformation nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL VIENNA UNIVERSITY OF TECHNOLOGY,
# DEPARTMENT OF GEODESY AND GEOINFORMATION BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


'''
In this module you will define several functions.

Please document your functions according to
https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
'''
# Example so that you can see a passing test
def f():
    """Returns the string 'success'
    """
    return "success"

##############################
# Basic function definitions #
##############################


# Define a function named add that takes two numbers and returns the sum.
def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters
    ----------
    a, b : int or float

    Returns
    -------
    int or float
    """
    return a + b


# Define a function named to_tuple that takes three arguments and returns a
# tuple of these three arguments.
def to_tuple(a, b, c):
    """
    Returns the arguments as a tuple.

    Parameters
    ----------
    a, b, c : int, float, string or list

    Returns
    -------
    tuple
    """
    return a, b, c


# Define a function named check5 that checks if a number is greater than 5 and
# returns True or False.
def check5(num):
    """
    This function determines whether a number is greater than 5.

    Parameters
    ----------
    num : int or float

    Returns
    -------
    boolean
    """
    return num > 5


# Define a function named check_n that check is a number is greater than n. The
# number should be the first argument and n the second
def check_n(num, threshold):
    """
    This function determines whether a number is greater than a threshold.

    Parameters
    ----------
    num , threshold : int or float

    Returns
    -------
    boolean
    """
    return num > threshold


#########
# LISTS #
#########

# Define a function named check_list that takes two arguments. The first
# argument is a list of numbers and the second argument is the number n to
# compare against. The function should return a list with equal length as the
# input list containing for each number in the original list either True or
# False if the number was greater than or equal to n.
def check_list(l, n):
    """
    This function determines if elements of a list are greater than or equal
    to a threshold.

    Parameters
    ----------
    l : list of int or float
    n : int or float
        threshold to be compared against

    Returns
    -------
    test : list of boolean
    """
    test = [x >= n for x in l]
    return test


# Define a function named check_list_nth that does the same as check_list but
# uses every nth element of the input list (including the first one). You will
# need a third input argument.
def check_list_nth(l, n, nth):
    """
    This function determines for every nth element of a list if the element
    is greater than or equal to a threshold.

    Parameters
    ----------
    l : list of int or float
    n : int or float
        threshold to be compared against
    nth : int
        Increment for the choice of list elements.

    Returns
    -------
    test : list of boolean
        Length of test is equal to the length of the list that contains only
        every nth element of the input list.
    """
    l = l[::nth]
    test = [x >= n for x in l]
    return test


# Define a function named add_new_list that takes two inputs. A list l and a
# second variable x to add to the list. Return a new list containing x as the
# last element without modifying the original list.
def add_new_list(l, x):
    """
    Returns a list containing the elements of the two input lists.

    Parameters
    ----------
    l, x : list

    Returns
    -------
    l_out : list
    """
    l_out = l.copy()
    l_out.append(x)
    return l_out


# Define a function named remove_nth that takes a list and removes every nth
# element (including the first one). Use a keyword named nth to set the default
# value for nth to 2.
def remove_nth(l, nth=2):
    """
    Returns a list where every nth element of the input list is removed.

    Parameters
    ----------
    l : list
    nth : int, optional
        Increment for the choice of list elements to be removed from list l.
        Default is 2.

    Returns
    -------
    l_out : list
    """
    l_out = l.copy()
    del l_out[::nth]
    return l_out


# Define a function named search_n that takes a list and a variable x and
# searches for x in the list. If the variable is found return the index of the
# variable in the list and the variable. Otherwise use None for both return
# values
def search_n(l, x):
    """
    Returns the position of x in list l and the value of x.

    Parameters
    ----------
    l : list
    x : int, float or str

    Returns
    -------
    i : int
        Position of x in list l.
        If x is not element of l, i is None.
    val : int, float or str
        Value of x.
        If x is not element of l, val is None.
    """
    i = None
    val = None
    if x in l:
        i = l.index(x)
        val = x
    return i, val


################
# Dictionaries #
################

# Define a function named args_to_dict that takes three arguments and returns a
# dictionary with the position of the argument as the key (starting at 0) and
# the argument as the value.
def args_to_dict(a, b, c):
    """
    Returns a dictionary containing the input arguments as values and
    their position as keys.

    Parameters
    ----------
    a, b, c : int, float or str

    Returns
    -------
    d : dict
    """
    d = {index: value for index, value in enumerate([a, b, c])}
    return d


# BONUS: Write a function named args_to_dict_general that does the same for any
# number of arguments
def args_to_dict_general(*args):
    """
    Returns a dictionary containing the input arguments as values and
    their position as keys.

    Parameters
    ----------
    args : int, float or str

    Returns
    -------
    d : dict
    """
    d = {index: value for index, value in enumerate(args)}
    return d


# Define a function named lists_to_dict that takes two lists of equal lenght
# named keys and values and builds a dictionary out of them.
def lists_to_dict(keys, values):
    """
    Returns a dictionary containing the input lists as keys and values.

    Parameters
    ----------
    keys, values : list

    Returns
    -------
    d : dict
    """
    d = {key: values[index] for index, key in enumerate(keys)}
    return d


# Define a function named search_list that takes two lists a and b. The
# function searches for all elements of b in list a. The return value should be
# a dictionary containing the index of the found element of b in list a and the
# value of the found element. If nothing was found then return an empty
# dictionary.
def search_list(a, b):
    """
    Returns the position for list elements of b in list a.

    Parameters
    ----------
    a, b : list

    Returns
    -------
    d : list
        Default is an empty list.
    """
    index = []
    values = []
    for x in b:
        if x in a:
            i = a.index(x)
            index.append(i)
            values.append(x)
    d = lists_to_dict(index, values)
    return d


# Define a function named dict_to_string that takes a dictionary and a
# separator string. The function should only take elements out of the
# dictionary whose value is a string and then return a single string containing
# the strings stored in the dictionary seperated by the separator string.
# Return an empty string if there are no strings in the dictionary.
def dict_to_string(d, s):
    """
    Returns all strings contained in the values of the dictionary as a single
    string seperated by a specified delimiter.

    Parameters
    ----------
    d : dict
    s : str
        Delimiter.

    Returns
    -------
    str_out : str
        Returns an empty string if the dictionary values do not
        contain any strings.
    """
    y = []
    for x in d.values():
        if isinstance(x, str):
            y.append(x)
    str_out = s.join(y)
    return str_out


# Define a function named classify_by_type which takes a list l and returns a
# dictionary d. The d must have the keys 'int' and 'str' which contain the
# elements out of l that have this type. Elements that do not fit one of these
# two types should be stored in a list under the key 'others'
def classify_by_type(l):
    """
    Returns a dictionary containing the elements of list l assigned to the keys
    'int', 'str' or 'others' according to the data types of the list elements.

    Parameters
    ----------
    l : list

    Returns
    -------
    d : dict
        Keys are 'int', 'str' and 'others'.
    """
    d = dict.fromkeys(['int', 'str', 'others'])
    for i in d.keys():
        d[i] = []
    for x in l:
        if isinstance(x, str):
            d['str'].append(x)
        elif isinstance(x, int):
            d['int'].append(x)
        else:
            d['others'].append(x)
    return d
