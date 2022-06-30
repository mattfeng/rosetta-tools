#!/usr/bin/env python
#
# (c) Copyright Rosetta Commons Member Institutions.
# (c) This file is part of the Rosetta software suite and is made available under license.
# (c) The Rosetta software is developed by the contributing members of the Rosetta Commons.
# (c) For more information, see http://www.rosettacommons.org. Questions about this can be
# (c) addressed to University of Washington CoMotion, email: license@uw.edu.

# Author: Rahel Frick (frick.rahel@gmail.com)
# Author: Jeliazko Jeliazkov (jeliazkov@jhu.edu)

import os
import sys

# coordinate stdevs and means for plotting ideal distributions
# TODO calculate these from angles.sc file
lhoc_mus = { "dist": 14.6, # angstroms
                "Hopen": 97.2, # degrees
                "Lopen": 99.4, # degrees
                "pack": -52.3, # degrees
                }

lhoc_sigmas = { "dist": 0.34, # angstroms
                "Hopen": 2.63, # degrees
                "Lopen": 1.92, # degrees
                "pack": 3.86, # degrees
                }

# coordinate abbreviations
PA = 'VL_VH_packing_angle'
HOA = 'VL_VH_opening_angle'
LOA = 'VL_VH_opposite_opening_angle'
D = 'VL_VH_distance'
total = 'total_score'
name = 'description'
coordinates = [PA, LOA, HOA, D]

# paths and command lines
# find Rosetta relative script dir:
# Rosetta/main/source/scripts/python/public/plot_VL_VH_orientational_coordinates/
rosetta_path = os.path.join(os.path.abspath(__file__), "..", "..", "..", "..", "..", "..", "..")
rosetta_path = os.path.abspath(rosetta_path)

if rosetta_path:

    rosetta_database = rosetta_path + '/main/database/'

    angles_file = rosetta_path + '/tools/antibody/angles.sc'
    if not os.path.isfile(angles_file):
        sys.exit("Could not find angles.sc at: {}".format(angles_file))

    rosetta_LHOC = rosetta_path + '/main/source/bin/packing_angle.'

    platform = {"darwin": "macos", "linux": "linux", "win64": "windows"}[sys.platform]

    if platform=="windows":
        sys.exit("Script only runs on mac or linux... check your sys.platform")

    for compiler in ["gcc", "clang", "icc"]:
        ext = platform + compiler + "release"
        if os.path.isfile(rosetta_LHOC + ext):
            rosetta_LHOC += ext
            break

    if not os.path.isfile(rosetta_LHOC):
        sys.exit("Could not find packing_angle executable at: {}".format(rosetta_LHOC))


else:
    sys.exit("""
    Could not find Rosetta relative to this script.
    If you have moved the script, please fix line 41, above.
    Thanks. Exiting.
    """)


# color codes for models (What template do they come from?)
color_dict = {}
color_dict['0'] = (141, 211, 199)
color_dict['1'] = (255, 255, 179)
color_dict['2'] = (190, 186, 218)
color_dict['3'] = (251, 128, 114)
color_dict['4'] = (128, 177, 211)
color_dict['5'] = (253, 180, 98)
color_dict['6'] = (179, 222, 105)
color_dict['7'] = (252, 205, 229)
color_dict['8'] = (187, 187, 187)
color_dict['9'] = (187, 128, 189)

for i in color_dict.keys():
    r, g, b = color_dict[i]
    color_dict[i] = (r / 255., g / 255., b / 255.)

# xlim for plots
x_lower = { LOA: 85, HOA: 87, PA: -70, D: 13}
x_upper = { LOA: 110, HOA: 115, PA: -35, D: 17}

alpha1 = ['101', '106', '107']
alpha2 = ['206', '217', '218', '220', '221', '223', '226', '228']
