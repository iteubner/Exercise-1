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

from dateutil.relativedelta import relativedelta as rdelta
from datetime import time


'''
Exercises for using the datetime and the calendar module
'''
# Define a function named last_of_month that takes an argument dt of type date
# and returns a date object representing the last day of the month dt was in.
def last_of_month(dt):
    """
    Returns the last day of a month.
    
    Parameters
    ----------
    dt : datetime
    
    Returns
    -------
    lastday : datetime    
    """        
    lastday = dt + rdelta(months=1, days=-dt.day)
    return lastday

# Define a function named feed_the_gremlin which takes a time object as an
# argument. It should return False between midnight and 6:30AM and True
# otherwise.
def feed_the_gremlin(tt):
    """
    This function determines if a time object lies between 6:30AM and 0:00AM.
    
    Parameters
    ----------
    tt : time
    
    Returns
    -------
    test : boolean
    """
    test = not (tt < time(6, 30, 0) and tt > time(0, 0, 0))
    return test


# Define a function named how_long that takes two datetime objects dt and ref
# where ref is the reference datetime, calculates the difference between them and
# returns the difference as a string formatted like:
# "01 days, 01 minutes, 01 seconds until 2000-12-31 15:59:59"
# If ref is before dt then use 'since' instead of 'until'
def how_long(dt, ref):
    """
    Returns the difference between two dates as a string.
    
    Parameters
    ----------
    dt : datetime
        date
    ref : datetime
        reference date
    Returns
    -------
    string : string
    """
    s = "{} days, {} minutes, {} seconds {} {}"
    d = dt - ref
    sub = "since"
    if dt < ref:
        sub = "until"
        d = ref - dt
    string = s.format(d.days, d.seconds // 60, d.seconds % 60, sub, str(ref))
    if dt == ref:
        string = "Dates are the same"
    return string