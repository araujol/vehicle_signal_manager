#!/usr/bin/env python3
#
# Add signals to signal group
#

import ipc.vsi
import vsmlib.utils

ipc.vsi.init_group()
sig_num, _ = vsmlib.utils.parse_signal_num_file("signal_number_maps/samples.vsi")
ipc.vsi.add_signals_to_group(sig_num)
