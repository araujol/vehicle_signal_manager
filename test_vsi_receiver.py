#!/usr/bin/env python3
#
# Receive VSI signal
#

import sys
import vsi_py as vsi
import ipc.vsi
import vsmlib.utils

if len(sys.argv) > 1:
    ipc.vsi.WAIT = True

sig_num, _ = vsmlib.utils.parse_signal_num_file("signal_number_maps/samples.vsi")
ipc.vsi.set_signal_number_map(sig_num)

print(ipc.vsi.receive())
