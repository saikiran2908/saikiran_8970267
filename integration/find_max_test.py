import mxValue


def test_c_max():
	x = 2
	y = 5
	z = 8
	# Expected output
	expected_output = 8
	# Check if the function returns the correct output
	assert mxValue.maximum(x, y, z) == expected_output, "Output doesn't match the expected value"
	
