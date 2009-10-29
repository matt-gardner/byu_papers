#!/usr/bin/env python

from __future__ import division
from psodata import PSOData
from evilplot import Plot, Points, RawData

ITERATIONS = 500
SWARMSIZE = 52

FUNCTIONS = ['sphere', 'rastrigin', 'rosenbrock', 'griewank', 'ackley']

FUNCTION_RANGE = [(10 ** -20, 10 ** 5), (0, 300), (100, float(10 ** 10)),
        (10 ** -2, 500), (10 ** -2, 100)]

FUNCTION_LOGSCALE = [10, 0, 10, 10, 10]

SEPSO_FILE = '../sepso_reproduce/function/ring13particles'
PICKBEST_FILE = '../sepso_pickbest/function/ring13particles'
STANDARD_FILE = '../standardpso/function/ring52particles'

for f, function in enumerate(FUNCTIONS):
    sepso_data = PSOData(open(SEPSO_FILE.replace('function', function)))
    pickbest_data = PSOData(open(PICKBEST_FILE.replace('function', function)))
    standard_data = PSOData(open(STANDARD_FILE.replace('function', function)))
    sepso_points = []
    pickbest_points = []
    standard_points = []
    for i in xrange(1, ITERATIONS):
        evaluations = i * SWARMSIZE
        sepso_points.append((evaluations, sepso_data.average(i*2)))
        pickbest_points.append((evaluations, pickbest_data.average(i*2)))
        standard_points.append((evaluations, standard_data.average(i)))

    plot = Plot()
    plot.xmin = SWARMSIZE
    plot.xmax = ITERATIONS * SWARMSIZE
    plot.ymin = FUNCTION_RANGE[f][0]
    plot.ymax = FUNCTION_RANGE[f][1]
    plot.ylogscale = FUNCTION_LOGSCALE[f]
    plot.xlabel = 'Function Evaluations'
    plot.ylabel = 'Best Function Value'
    plot.title = 'Ring topology, 13 and 52 particles, function: %s' % function

    plot.append(Points(sepso_points, title='SEPSO', style='lines'))
    plot.append(Points(pickbest_points, title='SEPSO Pick Best', style='lines'))
    plot.append(Points(standard_points, title='Standard PSO', style='lines'))

    plot.show()

# vim: et sw=4 sts=4
