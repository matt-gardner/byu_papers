#!/usr/bin/env python

from __future__ import division
from psodata import PSOData
from evilplot import Plot, Points, RawData

ITERATIONS = 500
# How many high and low outliers to drop:
TRIM = 2
DATADIR = '/aml/home/mjg82/psodata/data/star/'
SWARMSIZES = [50, 100, 500, 1000, 4000]

pattern = DATADIR + '%sparticles/rastrigin.out20batches'

plot = Plot()
for swarmsize in SWARMSIZES:
    points = []
    data = PSOData(open(pattern % swarmsize))
    for i in xrange(1, ITERATIONS + 1):
        points.append((i, data.average(i)))
    plot.append(Points(points, title='%s particles' % swarmsize, style='lines'))


plot.xmin = 1
plot.xmax = ITERATIONS
#plot.xlogscale = 10
plot.ymin = 3
plot.ymax = 300
plot.ylogscale = 10
#plot.xtics = dict((x, x) for x in SWARMSIZES if x != 400)
plot.ytics = dict((x, x) for x in (5, 10, 20, 50, 100, 200))
plot.xlabel = 'Iterations'
plot.ylabel = 'Best Function Value'
plot.show()
plot.write('iters_rast.gpi')

# vim: et sw=4 sts=4
