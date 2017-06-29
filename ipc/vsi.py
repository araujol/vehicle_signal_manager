#  Copyright (C) 2017, Jaguar Land Rover
#
#  This program is licensed under the terms and conditions of the
#  Mozilla Public License, version 2.0.  The full text of the 
#  Mozilla Public License is at https://www.mozilla.org/MPL/2.0/
#

import vsi_py as vsi

# The module public interface consists of the following functions:
#
# send    - Function to send signal.
#           It takes signal ID and value as arguments.
#
# receive - Function to receive signal.
#           It returns the received message as a tuple of (ID, Value).

def send(signal, value):
    # Domain is it relevant?
    domain = 1

    # Signal ID is an integer.
    signal_id = int(signal)

    # The signal name should be mapped in this module.
    # Maybe it is a good idea to have a single module to map name/ID
    # that could be re-used by any plugin.
    #
    # The VSI API already seems to offer functions for name/ID manipulation.
    # Check src/signals.h functions:
    #    int vsi_name_string_to_id (...)
    #    int vsi_signal_id_to_string (...)
    signal_name = ""

    # VSI call to insert (send) signal.
    vsi.InsertSignalData(domain, signal_id, signal_name, value)

def receive():
    # This function should use the new functions with group support to monitor
    # group of signals.

    # List of signals that will be monitored.
    signals = []

    # API steps:
    # - Create a signal group.
    #
    # - Iterate over the signals list and add each signal to the signal group.
    #
    # - Listen for incoming signals from the group.
    #   Use the function "listening" to any signal on the signal group.
    #   The python equivalent to the C function:
    #      'int vsi_listen_any_in_group (...)' at src/signals.h
    #
    #   Following the C API, the Python listening function might also return
    #   the ID of the received signal, which then can be used later with the
    #   Python getSignalData function to retrieve the signal value.
    pass
