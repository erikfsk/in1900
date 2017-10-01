from numpy.lib.scimath import sqrt
import numpy

print type(sqrt(-1)),sqrt(-1)


def funksjon(jeg_tar_gjerne_imot_argumenter,gjerne_flere_argumenter=0):
	if (jeg_tar_gjerne_imot_argumenter>gjerne_flere_argumenter):
		return 1
	else:
		return 0

def test_funksjon(jeg_vil_IKKE_ha_argumenter=False):
	exact_list = [0,1]
	computed_list = [funksjon(0),funksjon(1)]
	for exact_i,computed_i in zip(exact_list,computed_list):
		assert exact_i == computed_i





def funksjon2(jeg_tar_gjerne_imot_argumenter,gjerne_flere_argumenter=0):
	if (jeg_tar_gjerne_imot_argumenter>gjerne_flere_argumenter):
		return float(1)
	else:
		return float(0)

def test_funksjon2(jeg_vil_IKKE_ha_argumenter=False):
	tol = 1E-5
	exact_list = [float(0),float(1)]
	computed_list = [funksjon2(0),funksjon2(1)]
	for exact_i,computed_i in zip(exact_list,computed_list):
		assert abs(exact_i-computed_i) < tol





def funksjon3(jeg_tar_gjerne_imot_argumenter,gjerne_flere_argumenter=0):
	if (jeg_tar_gjerne_imot_argumenter>gjerne_flere_argumenter):
		return 1
	else:
		return 0

def test_funksjon3(jeg_vil_IKKE_ha_argumenter=False):
	assert 0 == funksjon3(0) and 1 == funksjon3(1)

test_funksjon()
test_funksjon2()
test_funksjon3()

