import numpy

reactions = 77
comm_size = 10
batch_size = reactions / comm_size
print "Batch Size: ", batch_size

for rank in range(0, comm_size):
	offset = batch_size * rank
	print "My rank is: ", rank
	
	#for x in range(offset, offset + batch_size):
	#	print x
	if rank == 0:
		print "I do remaing work ..."
	
