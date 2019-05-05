# -*- coding: utf-8 -*-
"""
/***************************************************************************
 sentinel2Indices
                                 A QGIS plugin
 THis plugin creates Indices and Products for a sentinel-2 image
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-05-05
        copyright            : (C) 2019 by Bartosz Mazurkiewicz
        email                : bartoszmazurkiewicz899@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load sentinel2Indices class from file sentinel2Indices.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sentinel2_Indices import sentinel2Indices
    return sentinel2Indices(iface)