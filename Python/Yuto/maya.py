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

# ToDo: add random.seed(any number) so that behavior based on any random number
# generation in functions below is always the same when re-running the script

random.seed(30)

#########################################################
# methods
#########################################################


####################################################################
#
# mkbldgs ToDo: complete function
#
# create simple geometry and group under group named by grp_name argument
#
####################################################################
def mkbldgs(grp_name, cyl_name, cube_name):
    new_cyl = cmds.polyCylinder(r=0.2, ax=[0, 1, 0], cuv=4, ch=True, name=cyl_name)
    new_cube = cmds.polyCube(h=2, ax=[0, 1, 0], cuv=4, ch=True, name=cube_name)
    new_bldgs = new_cyl + new_cube

    cmds.group(new_bldgs, name=grp_name)
    nodeattr = "%s.translateY" % new_bldgs[0]
    cmds.setAttr(nodeattr, 0.5)

    cmds.xform(worldSpace=True, pivots=[0, 0, 0])
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
    return new_bldgs[0]


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
def mkGroundPlane(numrows=30, numcols=30, stepx=1, stepz=1):
    new_ground = cmds.polyPlane(
        w=numrows, h=numcols, sx=numrows, sy=numcols, name="GroundPlane"
    )
    # cmds.group(new_ground, name=grp_name)
    nodeattr = "%s.translateY" % new_ground[0]
    cmds.setAttr(nodeattr, 0.5)
    return new_ground[0]


def copy2vtx(bldg_grp, hide=True):
    vtx_list = cmds.xform("GroundPlane.vtx[*]", q=True, ws=True, t=True)
    #    points = []
    #    for i in range(len(vtx_list)):
    #        points.append(vtx_list)

    points = zip(*[iter(vtx_list)] * 3)

    # print(len(points))

    bldg_list = cmds.listRelatives(bldg_grp, type="transform")
    bldg_01 = bldg_list[0]
    bldg_02 = bldg_list[1]
    allgeo = []
    for xyz in points:
        selectGeo = random.randint(0, 1)
        if selectGeo == 1:
            newgeo = cmds.duplicate(bldg_01)
        else:
            newgeo = cmds.duplicate(bldg_02)

        cmds.move(xyz[0], xyz[1] + 0.5, xyz[2], newgeo[0], absolute=True)
        allgeo.append(newgeo[0])

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


def randgeo(city_grp=None):
    """Randomize scale on all geo under group.

    Args:
    city_grp: group node containing geo to randomize. If None then get geo from selection.
    """

    randVal = random.uniform(-1, 1)

    if not city_grp:
        allgeo = cmds.ls(sl=True)
    else:
        allgeo = cmds.listRelatives(city_grp, type="transform")

    for each in allgeo:
        this_scale = (
            round(random.uniform(0.5, 1.5) * randVal, 3),
            round(random.uniform(0.5, 2.0) * randVal, 3),
            round(random.uniform(0.5, 1.5) * randVal, 3),
        )
        cmds.scale(
            this_scale[0],
            this_scale[1],
            this_scale[2],
            each,
            scaleXYZ=True,
            absolute=True,
        )
        cmds.rotate(0, random.uniform(-3, 3), 0, each)
    return
