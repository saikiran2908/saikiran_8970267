import swap


def test_c_swap():
	x = 5
	y = 10
	result = swap.swap_no(x, y)

	assert result == 15, "Value of x is not correctly swapped"
