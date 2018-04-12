#!/usr/bin/env python

# ex_function.py - example for function

pi = 3.141

def krog_obseg(rr):
    # rr - radij kroga
    # funkcija vrne obseg kroga, to je 2*pi*radij
    obseg = 2 * pi * rr
    return obseg


def main():
    radij1 = 10
    obseg1 = krog_obseg(radij1) # rezultat bo priblizno 62.82
    print "krog1 - radij1=%f, obseg1=%f\n" % (radij1, obseg1)

    radij1 = 35
    obseg1 = krog_obseg(radij1) # rezultat bo priblizno 219.87
    print "krog2 - radij1=%f, obseg1=%f\n" % (radij1, obseg1)

main()

#
