with open("ex26_sample.txt", "r") as f:
    print(f.read())

assert "%d" % 45 == '45'
assert "%i" % 45 == '45'
assert "%o" % 1000 == '1750'
assert "%u" % -1000 == '-1000'
assert "%x" % 1000 == '3e8'
assert "%X" % 1000 == '3E8'
assert "%e" % 1000 == '1.000000e+03'
assert "%E" % 1000 == '1.000000E+03'
assert "%f" % 10.34 == '10.340000'
assert "%F" % 10.34 == '10.340000'
assert "%g" % 10.34 == '10.34'
assert "%G" % 10.34 == '10.34'
assert "%c" % 34 == '"'
assert "%s there" % 'hi' == 'hi there'
assert "%r" % int == "<class 'int'>"
assert "%g%%" % 10.34 == '10.34%'

print(2**2)
print(2**3)
print(2//4)
print(4//2)
print(4//3)
print(4%3)
print(4%2)
print(2%4)
