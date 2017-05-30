#John Veillette

import sys
import csv
import json

from drawing import ChiCanvas, ColorKey


MIN_RECT_SIDE=0.01
MIN_RECT_SIDE_FOR_TEXT=0.03
X_SCALE_FACTOR=12
Y_SCALE_FACTOR=8


def draw_treemap(t, 
                 bounding_rec_height=1.0,
                 bounding_rec_width=1.0,
                 output_filename=None):

    '''
    Draw a treemap and the associated color key

    Inputs:
        t: a tree

        bounding_rec_height: the height of the bounding rectangle.

        bounding_rec_width: the width of the bounding rectangle.

        output_filename: (string or None) the name of a file for
        storing a the image or None, if the image should be shown.
    '''

    c = ChiCanvas(X_SCALE_FACTOR, Y_SCALE_FACTOR)

    # define coordinates for the initial rectangle for the treemap
    x_origin_init_rect = 0
    y_origin_init_rect = 0
    height_init_rect = bounding_rec_height
    width_init_rect = bounding_rec_width



    calc_weight(t)
    rects = make_rects(t, x_origin_init_rect, y_origin_init_rect, width_init_rect, height_init_rect, 1)
    #draw rectangles
    codes = set()
    for rect in rects:
        codes.add(rect['code'])
    codes = list(codes)
    key = ColorKey(codes)
    for rect in rects:
        color = key.get_color(rect['code'])
        x = rect['x']
        y = rect['y']
        width = rect['width']
        height = rect['height']
        c.draw_rectangle(x, y, x + width, y + height, color)
        if (height >= MIN_RECT_SIDE_FOR_TEXT): #and (width >= height):
            c.draw_text(x + width/2, y + height/2, width, rect['label'])
        #elif width >= MIN_RECT_SIDE_FOR_TEXT:
        #    c.draw_text_vertical(x + width/2, y + height/2, height, rect['label'])

    # save or show the result.
    if output_filename:
        print("saving...", output_filename)
        c.savefig(output_filename)
    else:
        c.show()


def calc_weight(t):
    '''
    Calculates and sets the weight of treenode t if the treenode's
    weight is not preassigned.

    Inputs: treenode t

    Returns:
        The weight of the treenode
    '''
    if t.weight == 0:
        w = 0 #sum the weight of the children
        children = t.get_children_as_list()
        for index in range(len(children)):
            w += calc_weight(children[index])
        t.weight = w
    return t.weight

def make_rects(t, x_orig, y_orig, init_width, init_height, orient):
    '''
    Returns a list of rectangles representing t

    Inputs
        t: a treenode
        x_orig: x position of the origin of intial rectangle
        y_orig: y position of the origin of initial rectangle
        init_height: height of initial rectangle
        init_width: width of initial rectangle
        orient: positive int if to initial rectangle to be broken
                horizontally, negative if vertically

    Returns: a list of dicts that represent rectangles
    '''
    if (not t.get_children_as_list()) or (init_width < MIN_RECT_SIDE) or (init_height < MIN_RECT_SIDE):
        rect = {}
        rect['code'] = t.code
        rect['x'] = x_orig
        rect['y'] = y_orig
        rect['height'] = init_height
        rect['width'] = init_width
        rect['label'] = t.label
        return [rect]
    else:
        rects = []
        x = x_orig
        y = y_orig
        for tree in t.get_children_as_list():
            ratio = tree.weight/t.weight
            if orient > 0:
                width = init_width * ratio
                height = init_height
                rects += make_rects(tree, x, y, width, height, -orient)
                x += width
            else:
                width = init_width
                height = init_height * ratio
                rects += make_rects(tree, x, y, width, height, -orient)
                y += height
        return rects