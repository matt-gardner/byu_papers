#!/usr/bin/env python

from __future__ import division
from psodata import PSOData
from evilplot import Plot, Points, RawData

ITERATIONS = 1000
SWARMSIZE = 50

SEPSO_FILE = '../sepso_reproduce/griewank/ring50particles'
PICKBEST_FILE = '../sepso_pickbest/griewank/ring50particles'
STANDARD_RAND = '../standardpso/griewank/ring200particles'

sepso_data = PSOData(open(SEPSO_FILE))
pickbest_data = PSOData(open(PICKBEST_FILE))
ring_data = PSOData(open(STANDARD_RAND))
sepso_points = []
pickbest_points = []
ring_points = []
for i in xrange(1, ITERATIONS):
    evaluations = i * SWARMSIZE
    sepso_points.append((evaluations, sepso_data.average(i*2)))
    pickbest_points.append((evaluations, pickbest_data.average(i*2)))
    ring_points.append((evaluations, ring_data.average(i)))

plot = Plot()
plot.xmin = SWARMSIZE
plot.xmax = ITERATIONS * SWARMSIZE
plot.ymin = 10 ** -9
plot.ymax = 500
plot.ylogscale = 10
plot.xlabel = 'Function Evaluations'
plot.ylabel = 'Best Function Value'

plot.append(Points(sepso_points, title='SEPSO', style='lines'))
plot.append(Points(pickbest_points, title='SEPSO Pick Best', style='lines'))
plot.append(Points(ring_points, title='PSO Ring', style='lines'))

plot.show()
plot.write('griewank1.gpi')

# vim: et sw=4 sts=4
