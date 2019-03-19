from behave import register_type
from behave import given,then,when
from hamcrest import assert_that,equal_to
import calculator

def parse_number(text):

    return int(text)


register_type(Number=parse_number)


@given("I have a calculator")
def step_impl(context):
    context.calc = calculator.Calculator()


@when('I add "{x:Number}" and "{y:Number}"')
def step_impl(context,x,y):
    assert isinstance(x,int)
    assert isinstance(y,int)
    context.calc.add2(x,y)


@then('the calculator returns "{expected:Number}"')
def step_impl(context,expected):
    assert isinstance(expected,int)
    assert_that(context.calc.result, equal_to(expected))
