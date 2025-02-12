from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 29
	assert simple_work_calc(20, 3, 2) == 85
	assert simple_work_calc(30, 4, 2) == 161

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 1670
	assert work_calc(30, 3, 2, lambda n: n) == 269


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2
	work_fn1 = lambda n: work_calc(n, 2, 2, lambda n: n)
	work_fn2 = lambda n: work_calc(n, 2, 2, lambda n: n**2)

res = compare_work(work_fn1, work_fn2)
print_results(res)

	
def test_compare_span():
	for n, w1, w2 in res:
		assert w1<w2
