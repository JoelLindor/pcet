from calc import doathing

# test a space in the input
test0 = doathing(" 2")
# test invalid input of non digit
test1 = doathing("Jimmy")

# test invalid input of a number < 0 or > 4
test2 = doathing("5")
test3 = doathing(0)
test4 = doathing("709w283475982w37498qw27")
