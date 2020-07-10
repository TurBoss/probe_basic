#!/usr/bin/env python

import os

from qtpyvcp.utilities import logger
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

import probe_basic_latc_rc

LOG = logger.getLogger('QtPyVCP.' + __name__)

VCP_DIR = os.path.abspath(os.path.dirname(__file__))


class ProbeBasicLATC(VCPMainWindow):
    """Main window class for the ProbeBasic VCP."""
    def __init__(self, *args, **kwargs):
        super(ProbeBasicLATC, self).__init__(*args, **kwargs)
