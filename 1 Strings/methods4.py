#rjust()   ljust()   center()
test = 'hello'

print(test.rjust(10))
print(test.ljust(10))
print(test.center(10))

print(test.rjust(10, "#"))
print(test.ljust(10, "%"))
print(test.center(11, "@"))

print("----------------------------------")
# expandtaps

test2  = 'Hello\tmy name\tis amoor\thow are you.'
print(test2)
print(test2.expandtabs(10))







