from behave import *

use_step_matcher("re")


@when("I create meme")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('I\'m viewing the details page for meme by "user"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("there are 1 memes")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("There are 0 memes")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass