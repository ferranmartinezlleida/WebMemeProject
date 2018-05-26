from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")

@given('Exists restaurant registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from Main_Meme.models import Meme
    for row in context.table:
        meme = Meme(user=user)
        for heading in row.headings:
            setattr(meme, heading, row[heading])
        meme.save()

@when('I create meme')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('memes:restaurant_create'))
        if context.browser.url == context.get_url('memes:restaurant_create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Upload').first.click()

@then('There are {count:n} memes')
def step_impl(context, count):
    from Main_Meme.models import Meme
    assert count == Meme.objects.count()

@then('I\'m viewing the details page for meme by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from Main_Meme.models import Meme
    meme = Meme.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(meme)

@when('I edit the meme with name "{name}"')
def step_impl(context, name):
    from Main_Meme.models import Meme
    restaurant = Meme.objects.get(name=name)
    context.browser.visit(context.get_url('myrestaurants:restaurant_edit', restaurant.pk))
    if context.browser.url == context.get_url('myrestaurants:restaurant_edit', restaurant.pk)\
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        context.browser.find_by_css('button.btn-success').first.click()