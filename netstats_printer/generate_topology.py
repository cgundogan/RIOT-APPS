#!/usr/bin/env python3

# Copyright (C) 2016 Cenk Gündoğan <mail@cgundogan.de>
#
# This file is subject to the terms and conditions of the GNU Lesser
# General Public License v2.1. See the file LICENSE in the top level
# directory for more details.

import os
import sys
import random

header_pre = '''\
<?xml version="1.0" encoding="UTF-8"?>
<topology version="1">
    <net description="{0} nodes in a star topology" name="star{0}">
        <nodeTypes>
            <nodeType name="riot_native">
                <interfaces>
                    <interface name="cc2420" type="802.15.4"/>
                </interfaces>
            </nodeType>
        </nodeTypes>
        <nodes>
            <node binary="{1}/bin/native/netstats_printer.elf" name="a1" type="riot_native"/>\
'''

header_post = '''\
        </nodes>
        <links>\
'''

footer = '''\
        </links>
    </net>
</topology>\
'''

node = '            <node binary="{0}/bin/native/netstats_printer.elf" name="{1}" type="riot_native"/>'
link = '            <link broadcast_loss="0.0" from_if="cc2420" from_node="{0}" loss="0.0" to_if="cc2420" to_node="{1}" uni="false"/>'


def print_topology(numNodes):

    print(header_pre.format(numNodes, os.getcwd()))

    for i in range(numNodes):
        print(node.format(os.getcwd(), "a" + str(i + 2)))

    print(header_post)

    for i in range(numNodes):
        print(link.format("a1", "a" + str(i + 2)))

    print(footer)

if __name__ == "__main__":
   print_topology(int(sys.argv[1]))
