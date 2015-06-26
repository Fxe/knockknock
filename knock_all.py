import numpy
import cobra, cobra.test, libsbml

model = cobra.test.create_test_model(cobra.test.ecoli_pickle)

for x in model.reactions:
	print x.lower_bound, x.upper_bound
	print "knock out:", x
	lb = x.lower_bound
	ub = x.upper_bound
	x.lower_bound = 0
	x.upper_bound = 0
	model.optimize()
	status = model.solution.status
	value = model.solution.f
	print status, value
	x.lower_bound = lb
	x.upper_bound = ub
	break
