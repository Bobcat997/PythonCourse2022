# import test as finder
import example_package.module2 as epn
from test import find_longest_word, show

from random import choice
items = ['tent', 'bidon', 'glasses', 'mug']


longest_word = find_longest_word(items)
show(longest_word)
print(epn.get_name())