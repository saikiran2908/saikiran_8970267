import swap


def c_swap():
	x = 5
	y = 10
	result = swap.swap_no(x, y) == 15

	assert result == 15, "Value of x is not correctly swapped"
