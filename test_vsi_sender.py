#!/usr/bin/env python3
#
# Send VSI signal
#

import vsi_py as vsi
import ipc.vsi
import vsmlib.utils

sig_num, _ = vsmlib.utils.parse_signal_num_file("signal_number_maps/samples.vsi")
ipc.vsi.set_signal_number_map(sig_num)

ipc.vsi.send("transmission.gear", "forward")
