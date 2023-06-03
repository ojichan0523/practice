#!/usr/bin/env python
"""
   Generate a cityscape from simple geometry copied to grid or surface.
   
   File: makecity.py
   Version: 2.0
   Date: Oct 18, 2019
   Author: Suzanne Berger
   Contact: zanefx7@gmail.com
"""
import sys
import random
import logging
from pprint import pprint

import maya.cmds as cmds


#########################################################
# globals
#########################################################

VERSION = "V02"
logging.basicConfig(level=logging.INFO)
logging.info("makecity.py Version %s" % VERSION)

#ToDo: add random.seed(any number) so that behavior based on any random number
#generation in functions below is always the same when re-running the script

#########################################################
# methods
#########################################################


def mkcube(grp_name, cube_name):
    """ Make cube under group node at origin with dimension 1,1,1 and pivot at origin.
        
        Args:
        grp_name: object name of parent group to contain cube
        cube_name: object name of cube node
        
        Example:
        makecity.mkcube("building_grp", "cube0")
    """
    new_cube = cmds.polyCube(ax=[0, 1, 0], cuv=4, ch=True, name=cube_name)
    cmds.group(new_cube, name=grp_name)
    nodeattr = "%s.translateY" % new_cube[0]
    cmds.setAttr(nodeattr, 0.5)
    
    # another way to change pivot on geo
    #spattr = "%s.scalePivot" % new_cube[0]
    #rpattr = "%s.rotatePivot" % new_cube[0]
    #cmds.move(0, 0, 0, spattr, rpattr, absolute=True)
    
    # ToDo: fix bug so that pivot xform applies to cube and not group node
    cmds.xform(worldSpace=True, pivots=[0,0,0])
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1 )
    return new_cube[0]


####################################################################
#
# mkbldgs ToDo: complete function
#
# create simple geometry and group under group named by grp_name argument
#
####################################################################
def mkbldgs(grp_name):
    """
        !!! Not implemented yet !!!
        
        Args:
        bldg_grp: group node name to contain building geos
    """
    logging.info("mkbldgs: !!! Not implemented yet !!!")
    return


def copy2grid(bldg_grp, numrows=4, numcols=4, stepx=3, stepz=3, hide=True):
    """ Duplicate geo over grid.
        
        Total number of copies = numrows * numcols.
        
        Args:
        bldg_grp: group node containing geo to be copied
        numrows: number of rows in grid, default = 4
        numcols: number of columns in grid, default = 4
        stepx: x translate step for each geo copy, default = 3
        stepz: z translate step for each geo copy, default = 3
        hide: Booleon to hide original geo after copies completed, default = True
        
        Example:
        newcity = makecity.copy2grid("building_grp")
    """
    
    # create list of xyz points of grid where each xyz point in list is a tuple
    # ToDo: replace logic that builds list with list comprehension
    points = []
    for i in range(numcols):
        for j in range(numrows):
            x = stepx * i
            z = stepz * j
            points.append((x,0,z))
    pprint(points)     # debug check of list of point tuples

    # get building geo under bldg_grp and copy to each point of grid
    # ToDo: if more than 1 geo under group, use random.choice(bldg_list)
    # to get random choice building geo to be copied.
    bldg_list = cmds.listRelatives(bldg_grp, type="transform")
    this_bldg = bldg_list[0]
    allgeo = []
    for xyz in points:
        newgeo = cmds.duplicate(this_bldg)
        cmds.move(xyz[0], xyz[1], xyz[2], newgeo[0], absolute=True)
        allgeo.append(newgeo[0])

    # group all copies under city_grp
    #pprint(allgeo)    # debug check of allgeo list
    city_grp = cmds.group(allgeo, name="city_grp", w=True)
    
    # turn off original geo's visibility if hide is True
    if hide:
        cmds.setAttr("%s.visibility" % bldg_grp, 0)
    return city_grp


####################################################################
#
# copy2vtx ToDo: complete function
#
# test whether geo is nurbs or poly mesh then use one of these code snippets
# to create list of points for duplication like code in copy2grid
#
# vtx_list = cmds.xform('cube0.vtx[*]', q=True, ws=True, t=True)
# points = [(vtx_list[i], vtx_list[i+1], vtx_list[i+2]) for i in range(0,len(vtx_list),3)]
# !!! OR !!!
# points = zip(*[iter(vtx_list)]*3)
#
# cv_list = cmds.xform('nurbsSphere1.cv[*]', q=True, ws=True, t=True)
# points = [(cv_list[i], cv_list[i+1], cv_list[i+2]) for i in range(0,len(cv_list),3)]
# !!! OR !!!
# points = zip(*[iter(cv_list)]*3)
#
# pprint(points)
#
####################################################################

def copy2vtx(bldg_grp, obj):
    """ Copy geometry objects under bldg_grp to all surface points on obj.
        
        !!! Not implemented yet !!!
        
        Args:
        bldg_grp: group node containing geo to be copied
        obj: poly or nurbs surface containing position points for copy
        
        Example:
        new_city = makecity.copy2vtx("building_grp", "nurbsPlane1")
    """
    logging.info("copy2vtx: !!! Not implemented yet !!!")
    return


###############################################################################
#
# randgeo ToDo: add optional arguments and functionality
#   - add optional arguments for range values to randomize scale
#   - use hard-coded args in random.uniform as default values to randomize scale
#   - add optional arguments to randomize rotation or do not randomize rotation at all
#
#
###############################################################################

def randgeo(city_grp = None):
    """ Randomize scale on all geo under group.
        
        Args:
        city_grp: group node containing geo to randomize. If None then get geo from selection.
    """
    if not city_grp:
        allgeo = cmds.ls(sl=True)
    else:
        allgeo = cmds.listRelatives(city_grp, type="transform")
    
    for each in allgeo:
        this_scale = (round(random.uniform(0.5, 1.5), 3),
                      round(random.uniform(0.5, 2.0), 3),
                      round(random.uniform(0.5, 1.5), 3))
        cmds.scale(this_scale[0], this_scale[1], this_scale[2], each, scaleXYZ=True, absolute=True)
    return