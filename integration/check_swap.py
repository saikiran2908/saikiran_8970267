import swap

def c_swap():
	x = 5
	y = 10
	swap.swap_no(x,y)

	assert x == 10, "Value of x is not correctly swapped"
	assert y == 5, "Value of y is not correctly swapped"