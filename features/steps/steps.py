from behave import *
from calculator import *

@given('an empty string')
def impl_bk(context):
    print('')
@when('the string is calculated')
def impl_bk(context):
    print('calculating')
@then('the result is 0')
def impl_bk(context):
    value = string_calculator('')
    assert value == 0


@given('a string {string}')
def impl_bk(context, string):
    print("string  = '" + string + "'")

@then('the result is 3')
def impl_bk(context):
    value = string_calculator("1,2")
    assert value == 3

@then('the result is 8')
def impl_bk(context):
    value = string_calculator("1,2,5")
    assert value == 8

@then('the calculation of the string throws a NegativeNumberNotAllowed exception')
def impl_bk(context):
    value = string_calculator("1,2,-3")
    assert value == 0
    