#!/bin/sh

if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

LINKS=10
python generate_topology.py ${LINKS} > grid16_${LINKS}.xml
mv grid16_${LINKS}.xml RIOT/dist/tools/desvirt/desvirt/.desvirt

make clean all
TOPO=grid16_${LINKS}.xml make desvirt-define
TOPO=grid16_${LINKS}.xml make desvirt-start

PORT_ROOT=$(ps au | grep grid16_a1 | grep TCP-L | awk -F, '{  print $4 }' | cut -d\: -f 2)
echo ${PORT_ROOT}
echo "ifconfig 5 add abcd::1" | nc localhost ${PORT_ROOT} > /dev/null
echo "rpl root 1 abcd::1" | nc localhost ${PORT_ROOT} > /dev/null

#TOPO=grid16_${LINKS}.xml make desvirt-stop
#TOPO=grid16_${LINKS}.xml make desvirt-undefine
