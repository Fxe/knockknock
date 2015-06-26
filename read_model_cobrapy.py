import numpy
import cobra, libsbml

model = cobra.io.read_sbml_model("/home/fliu/data/sbml/Ec_core_flux1.xml")

print "Reactions: ", len(model.reactions)
print "Species: ", len(model.metabolites)

model.optimize()

print "Obj: ", model.solution.f
