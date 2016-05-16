#!/usr/bin/env python3

# Copyright (C) 2016 Cenk Gündoğan <mail@cgundogan.de>
#
# This file is subject to the terms and conditions of the GNU Lesser
# General Public License v2.1. See the file LICENSE in the top level
# directory for more details.

import os
import sys
import random

header = '''\
<?xml version="1.0" encoding="UTF-8"?>
<topology version="1">
    <net description="16 nodes in a regular 4x4 grid" name="grid16">
        <nodeTypes>
            <nodeType name="riot_native">
                <interfaces>
                    <interface name="cc2420" type="802.15.4"/>
                </interfaces>
            </nodeType>
        </nodeTypes>
        <nodes>
            <node binary="{0}/bin/native/udp_counter.elf" name="a1" type="riot_native"/>
            <node binary="{0}/bin/native/udp_counter.elf" name="a2" type="riot_native"/>
            <node binary="{0}/bin/native/udp_counter.elf" name="a3" type="riot_native"/>
            <node binary="{0}/bin/native/udp_counter.elf" name="a4" type="riot_native"/>
            <node binary="{0}/bin/native/udp_counter.elf" name="b1" type="riot_native"/>
            <node binary="{0}/bin/native/udp_counter.elf" name="b2" type="riot_native"/>
            <node binary="{0}/bin/native/udp_counter.elf" name="b3" type="riot_native"/>
            <node binary="{0}/bin/native/udp_counter.elf" name="b4" type="riot_native"/>
            <node binary="{0}/bin/native/udp_counter.elf" name="c1" type="riot_native"/>
            <node binary="{0}/bin/native/udp_counter.elf" name="c2" type="riot_native"/>
            <node binary="{0}/bin/native/udp_counter.elf" name="c3" type="riot_native"/>
            <node binary="{0}/bin/native/udp_counter.elf" name="c4" type="riot_native"/>
            <node binary="{0}/bin/native/udp_counter.elf" name="d1" type="riot_native"/>
            <node binary="{0}/bin/native/udp_counter.elf" name="d2" type="riot_native"/>
            <node binary="{0}/bin/native/udp_counter.elf" name="d3" type="riot_native"/>
            <node binary="{0}/bin/native/udp_counter.elf" name="d4" type="riot_native"/>
        </nodes>
        <links>\
'''

footer = '''\
        </links>
    </net>
</topology>\
'''

links = (
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="a1" loss="0.0" to_if="cc2420" to_node="a2" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="a2" loss="0.0" to_if="cc2420" to_node="a1" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="a1" loss="0.0" to_if="cc2420" to_node="b1" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b1" loss="0.0" to_if="cc2420" to_node="a1" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="a1" loss="0.0" to_if="cc2420" to_node="b2" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b2" loss="0.0" to_if="cc2420" to_node="a1" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="a2" loss="0.0" to_if="cc2420" to_node="b1" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b1" loss="0.0" to_if="cc2420" to_node="a2" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="a2" loss="0.0" to_if="cc2420" to_node="b2" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b2" loss="0.0" to_if="cc2420" to_node="a2" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="a2" loss="0.0" to_if="cc2420" to_node="b3" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b3" loss="0.0" to_if="cc2420" to_node="a2" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="a2" loss="0.0" to_if="cc2420" to_node="a3" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="a3" loss="0.0" to_if="cc2420" to_node="a2" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="a3" loss="0.0" to_if="cc2420" to_node="b2" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b2" loss="0.0" to_if="cc2420" to_node="a3" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="a3" loss="0.0" to_if="cc2420" to_node="b3" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b3" loss="0.0" to_if="cc2420" to_node="a3" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="a3" loss="0.0" to_if="cc2420" to_node="b4" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b4" loss="0.0" to_if="cc2420" to_node="a3" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="a3" loss="0.0" to_if="cc2420" to_node="a4" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="a4" loss="0.0" to_if="cc2420" to_node="a3" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="a4" loss="0.0" to_if="cc2420" to_node="b3" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b3" loss="0.0" to_if="cc2420" to_node="a4" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="a4" loss="0.0" to_if="cc2420" to_node="b4" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b4" loss="0.0" to_if="cc2420" to_node="a4" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b1" loss="0.0" to_if="cc2420" to_node="b2" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b2" loss="0.0" to_if="cc2420" to_node="b1" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b1" loss="0.0" to_if="cc2420" to_node="c2" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c2" loss="0.0" to_if="cc2420" to_node="b1" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b1" loss="0.0" to_if="cc2420" to_node="c1" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c1" loss="0.0" to_if="cc2420" to_node="b1" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b2" loss="0.0" to_if="cc2420" to_node="b3" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b3" loss="0.0" to_if="cc2420" to_node="b2" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b2" loss="0.0" to_if="cc2420" to_node="c3" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c3" loss="0.0" to_if="cc2420" to_node="b2" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b2" loss="0.0" to_if="cc2420" to_node="c2" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c2" loss="0.0" to_if="cc2420" to_node="b2" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b2" loss="0.0" to_if="cc2420" to_node="c1" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c1" loss="0.0" to_if="cc2420" to_node="b2" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b3" loss="0.0" to_if="cc2420" to_node="b4" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b4" loss="0.0" to_if="cc2420" to_node="b3" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b3" loss="0.0" to_if="cc2420" to_node="c4" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c4" loss="0.0" to_if="cc2420" to_node="b3" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b3" loss="0.0" to_if="cc2420" to_node="c3" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c3" loss="0.0" to_if="cc2420" to_node="b3" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b3" loss="0.0" to_if="cc2420" to_node="c2" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c2" loss="0.0" to_if="cc2420" to_node="b3" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b4" loss="0.0" to_if="cc2420" to_node="c4" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c4" loss="0.0" to_if="cc2420" to_node="b4" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="b4" loss="0.0" to_if="cc2420" to_node="c3" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c3" loss="0.0" to_if="cc2420" to_node="b4" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c1" loss="0.0" to_if="cc2420" to_node="c2" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c2" loss="0.0" to_if="cc2420" to_node="c1" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c1" loss="0.0" to_if="cc2420" to_node="d2" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="d2" loss="0.0" to_if="cc2420" to_node="c1" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c1" loss="0.0" to_if="cc2420" to_node="d1" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="d1" loss="0.0" to_if="cc2420" to_node="c1" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c2" loss="0.0" to_if="cc2420" to_node="c3" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c3" loss="0.0" to_if="cc2420" to_node="c2" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c2" loss="0.0" to_if="cc2420" to_node="d3" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="d3" loss="0.0" to_if="cc2420" to_node="c2" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c2" loss="0.0" to_if="cc2420" to_node="d2" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="d2" loss="0.0" to_if="cc2420" to_node="c2" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c2" loss="0.0" to_if="cc2420" to_node="d1" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="d1" loss="0.0" to_if="cc2420" to_node="c2" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c3" loss="0.0" to_if="cc2420" to_node="c4" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c4" loss="0.0" to_if="cc2420" to_node="c3" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c3" loss="0.0" to_if="cc2420" to_node="d4" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="d4" loss="0.0" to_if="cc2420" to_node="c3" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c3" loss="0.0" to_if="cc2420" to_node="d3" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="d3" loss="0.0" to_if="cc2420" to_node="c3" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c3" loss="0.0" to_if="cc2420" to_node="d2" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="d2" loss="0.0" to_if="cc2420" to_node="c3" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c4" loss="0.0" to_if="cc2420" to_node="d4" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="d4" loss="0.0" to_if="cc2420" to_node="c4" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="c4" loss="0.0" to_if="cc2420" to_node="d3" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="d3" loss="0.0" to_if="cc2420" to_node="c4" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="d1" loss="0.0" to_if="cc2420" to_node="d2" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="d2" loss="0.0" to_if="cc2420" to_node="d1" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="d2" loss="0.0" to_if="cc2420" to_node="d3" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="d3" loss="0.0" to_if="cc2420" to_node="d2" uni="true"/>',

'            <link broadcast_loss="0.0" from_if="cc2420" from_node="d3" loss="0.0" to_if="cc2420" to_node="d4" uni="true"/>',
'            <link broadcast_loss="0.0" from_if="cc2420" from_node="d4" loss="0.0" to_if="cc2420" to_node="d3" uni="true"/>',
)


def print_topology(numLinks):
    unidir = sorted(random.sample(range(0,int(len(links)/2)), numLinks))

    print(header.format(os.getcwd()))

    i = 0
    while i < len(links)/2:
        if i in unidir:
            print(links[i*2+random.randint(0,1)])
        else:
            print(links[i*2])
            print(links[i*2+1])

        i = i + 1

    print(footer)

if __name__ == "__main__":
   print_topology(int(sys.argv[1]))
