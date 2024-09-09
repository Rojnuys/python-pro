import re


def new_format(string):
    return re.sub(r"(?P<part>\d{3}(?=.))", r"\g<part>.", string[::-1])[::-1]


assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")
assert (new_format("1234456") == "1.234.456")

print("All tests passed")
