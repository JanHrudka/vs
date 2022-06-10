#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Pomocné knihovny
import argparse
import turtle as T
import math

parser = argparse.ArgumentParser()
parser.add_argument('-r', default = 100, type = int, help = 'R')
parser.add_argument('-e', default = 12, type = int, help = 'edges')
parser.add_argument('-s', default = 10, type = int, help = 'speed')

t = T.Turtle()

def draw_leaf(x, R):
    """ Kresba lístku """
    t.penup()
    t.forward(x)
    t.right(90)
    t.forward(R)
    t.left(90)
    t.pendown()
    t.circle(R, 180)
    t.penup()
    t.left(90)
    t.forward(R)
    t.right(90)
    t.forward(x)
    t.right(180)

def main(args):
    """ Hlavní funkce """
    t.speed(args.s)
    t.color('gray')
    R = args.r*math.sin((360/args.e/2)*math.pi/180)
    for edge in range(args.e):
        draw_leaf(args.r, R)
        t.right(360/args.e)

if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    main(args)
    input('Done!')
