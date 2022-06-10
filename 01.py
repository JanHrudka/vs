#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import turtle as T

parser = argparse.ArgumentParser()
parser.add_argument('-r', default = 100, type = int, help = 'R')
parser.add_argument('-e', default = 12, type = int, help = 'edges')

t = T.Turtle()

def draw_leaf(x):
    t.forward(x)
    t.left(30)
    t.right(60)
    t.left(30)
    t.backward(x)

def main(args):
    t.speed(100)
    t.color('gray')

    for edge in range(args.e):
        draw_leaf(args.r)
        t.right(360/args.e)

if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    main(args)
    input('Done!')
