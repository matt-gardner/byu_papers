#!/usr/bin/env python

from __future__ import division
from psodata import PSOData
from evilplot import Plot, Points, RawData

ITERATIONS = 500
DATADIR = '../../../psodata/data/'
K400_FILE = DATADIR + 'star/400particles/rastrigin.out20batches'
ISLANDS10_400_FILE = DATADIR + '10communicating_islands/4000particles/rastrigin.out20batches'

plot = Plot()

data = PSOData(open(K400_FILE))
points = []
for i in xrange(1, ITERATIONS + 1):
    points.append((i, data.average(i)))
plot.append(Points(points, title='Complete', style='lines'))

data = PSOData(open(ISLANDS10_400_FILE))
points = []
for i in xrange(1, ITERATIONS + 1):
    points.append((i, data.average(i)))
plot.append(Points(points, title='10 Subswarms of 400 particles', style='lines'))

plot.xmin = 100
plot.xmax = ITERATIONS
#plot.xlogscale = 10
plot.ymin = 3
plot.ymax = 50
plot.ylogscale = 10
#plot.xtics = dict((x, x) for x in SWARMSIZES if x != 400)
plot.ytics = dict((x, x) for x in (5, 10, 20, 50, 100, 200))
plot.xlabel = 'Iterations'
plot.ylabel = 'Best Function Value'
plot.show()
plot.write('islands_iters_rast.gpi')

# vim: et sw=4 sts=4
