# -*- coding: utf-8 -*-

"""
Created on 2013-02-23
:author: Andreas Kaiser (disko)
"""

from fanstatic import Library
from fanstatic import Resource


library = Library(
    'javascript_canvas_to_blob',
    'resources'
    )

canvas_to_blob = Resource(
    library,
    'canvas-to-blob.js',
    minified='canvas-to-blob.min.js'
    )
