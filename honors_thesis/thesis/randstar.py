#!/usr/bin/env python

from __future__ import division
from psodata import PSOData
from evilplot import Plot, Points

ITERATIONS = 500
# How many high and low outliers to drop:
TRIM = 2
DATADIR = '../../../psodata/data/'
SWARMSIZES = [50, 100, 200, 300, 400, 500, 1000, 2000, 4000]
#SWARMSIZES = [50, 100, 200, 300, 400, 500, 1000, 2000]

star_pattern = DATADIR + 'star/%sparticles/rastrigin.out20batches'
rand20_pattern = DATADIR + 'random20/%sparticles/rastrigin.out20batches'
rand5_pattern = DATADIR + 'random5/%sparticles/rastrigin.out20batches'
rand2_pattern = DATADIR + 'random2particles/%sparticles/rastrigin.out20batches'

star_points = []
star_bars = []
rand20_points = []
rand5_points = []
rand2_points = []
for swarmsize in SWARMSIZES:
    star_data = PSOData(open(star_pattern % swarmsize))
    star_points.append((swarmsize, star_data.average(ITERATIONS)))
    low, med, high = star_data.statistics(ITERATIONS, TRIM)
    print 'star:', swarmsize, low, med, high
    star_bars.append((swarmsize, med, low, high))

    rand20_data = PSOData(open(rand20_pattern % swarmsize))
    rand20_points.append((swarmsize, rand20_data.average(ITERATIONS)))

    rand5_data = PSOData(open(rand5_pattern % swarmsize))
    rand5_points.append((swarmsize, rand5_data.average(ITERATIONS)))

    rand2_data = PSOData(open(rand2_pattern % swarmsize))
    rand2_points.append((swarmsize, rand2_data.average(ITERATIONS)))

plot = Plot(xmin=45, xmax=4400, xlogscale=2, ymin=4, ymax=50, ylogscale=10)
plot.xtics = dict((x, x) for x in SWARMSIZES if x != 400)
plot.ytics = dict((x, x) for x in (5, 10, 20, 50))
plot.xlabel = 'Swarm Size'
plot.ylabel = 'Value after %s iterations' % ITERATIONS
plot.append(Points(star_points, style='lines', title='Complete'))
plot.append(Points(rand20_points, style='lines', 
    title='Random, 20% communication'))
plot.append(Points(rand5_points, style='lines', 
    title='Random, 5% communication'))
plot.append(Points(rand2_points, style='lines'
    , title='Random, only two neighbors'))
plot.show()
plot.write('randstar.gpi')

# vim: et sw=4 sts=4
