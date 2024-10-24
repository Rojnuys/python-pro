from words_generator import words_generator
from dict_map import DictMap


dd = {"a": 1, "b": 2, "c": 3}

for i in DictMap(dd, lambda key: key.upper(), lambda value: value ** 2):
    print(i)

print("--------------------------------")

for i in DictMap(dd, lambda key: key.upper(), lambda value: value ** 2):
    print(i)

print("--------------------------------")

for i in DictMap(dd, lambda key: key.upper(), lambda value: value ** 2):
    print(i)

print("--------------------------------")

for word in words_generator(10):
    print(word)

print("--------------------------------")

for word in words_generator(100):
    print(word)

print("--------------------------------")

for word in words_generator(1000):
    print(word)

print("--------------------------------")

for word in words_generator(10001):
    print(word)
