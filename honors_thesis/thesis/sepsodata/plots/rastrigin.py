#!/usr/bin/env python

from __future__ import division
from psodata import PSOData
from evilplot import Plot, Points, RawData

ITERATIONS = 1000
SWARMSIZE = 200

SEPSO_FILE = '../sepso_reproduce/rastrigin/rand200particles'
PICKBEST_FILE = '../sepso_pickbest/rastrigin/rand200particles'
STANDARD_RAND = '../standardpso/rastrigin/rand800particles'
STANDARD_RING = '../standardpso/rastrigin/ring800particles'
STANDARD_COMPLETE = '../standardpso/rastrigin/complete800particles'

sepso_data = PSOData(open(SEPSO_FILE))
#pickbest_data = PSOData(open(PICKBEST_FILE))
rand_data = PSOData(open(STANDARD_RAND))
#ring_data = PSOData(open(STANDARD_RING))
complete_data = PSOData(open(STANDARD_COMPLETE))
sepso_points = []
pickbest_points = []
rand_points = []
#ring_points = []
complete_points = []
for i in xrange(1, ITERATIONS):
    evaluations = i * SWARMSIZE
    sepso_points.append((evaluations, sepso_data.average(i*2)))
    #pickbest_points.append((evaluations, pickbest_data.average(i*2)))
    rand_points.append((evaluations, rand_data.average(i)))
    #ring_points.append((evaluations, ring_data.average(i)))
    complete_points.append((evaluations, complete_data.average(i)))

plot = Plot()
plot.xmin = SWARMSIZE
plot.xmax = ITERATIONS * SWARMSIZE
plot.ymin = 0
plot.ymax = 100
plot.xlabel = 'Function Evaluations'
plot.ylabel = 'Best Function Value'

plot.append(Points(sepso_points, title='SEPSO', style='lines'))
#plot.append(Points(pickbest_points, title='SEPSO Pick Best', style='lines'))
plot.append(Points(rand_points, title='PSO Random', style='lines'))
#plot.append(Points(ring_points, title='PSO Ring', style='lines'))
plot.append( Points(complete_points, title='PSO Complete', style='lines'))

plot.show()
plot.write('rastrigin.gpi')


# vim: et sw=4 sts=4
