"""
CEST Quantiphyse plugin

Author: Martin Craig <martin.craig@eng.ox.ac.uk>
Copyright (c) 2016-2017 University of Oxford, Martin Craig
"""
import os
import sys

from .widget import CESTWidget, get_model_lib

QP_MANIFEST = {
    "widgets" : [CESTWidget],
    "fabber-libs" : [get_model_lib("cest")]
}
