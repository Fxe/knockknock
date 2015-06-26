import time
import numpy
import cobra, libsbml
#import cobra.test
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

print "Comm World Size:", size
print "Hi I am ", name, " with rank ", rank
#model = cobra.test.create_test_model(cobra.test.ecoli_pickle)
model = cobra.io.read_sbml_model("/home/fliu/data/sbml/Ec_core_flux1.xml")

work = {}
work[rank] = []

reactions = len(model.reactions)
batch_size = reactions / size
print reactions, batch_size

print name, "Let me distribute some work"
for x in range(rank*batch_size, rank*batch_size + 40):
	work[rank].append(model.reactions[x])
print rank, " ", len(work[rank])

start = time.clock()
for x in work[rank]:
#	print x.lower_bound, x.upper_bound
#	print "knock out:", x
	lb = x.lower_bound
	ub = x.upper_bound
	x.lower_bound = 0
	x.upper_bound = 0
	model.optimize()
	status = model.solution.status
	value = model.solution.f
#	print status, x, value
	x.lower_bound = lb
	x.upper_bound = ub

print "process time: ", (time.clock() - start)
print name, "I am done today !"
