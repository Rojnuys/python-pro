from decimal import Decimal
from common import frange, colorizer

assert (list(frange(5)) == [0, 1, 2, 3, 4])
assert (list(frange(2, 5)) == [2, 3, 4])
assert (list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert (list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert (list(frange(1, 5)) == [1, 2, 3, 4])
assert (list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert (list(frange(0, 0)) == [])
assert (list(frange(100, 0)) == [])
assert (list(frange(Decimal(1), Decimal(10), Decimal(1.5))) == [Decimal('1'), Decimal('2.5'), Decimal('4.0'),
                                                                Decimal('5.5'), Decimal('7.0'), Decimal('8.5')])

with colorizer("lightgreen_ex"):
    print("SUCCESS!")

with colorizer("red"):
    print("TOTAL SUCCESS!")

print("The end of program")