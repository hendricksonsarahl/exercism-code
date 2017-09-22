def is_leap_year(year):
    '''A year is a leap year IF:
    year is divisble by 4
    year is divisble by 4 AND not divisible by 100
    year is divisble by 400'''

    return year % 4 == 0 and (
        year % 100 != 0 or year % 400 == 0)

is_leap_year(2015)
