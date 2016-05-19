#!/bin/sh

if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

[[ -d desvirt_topologies ]] || mkdir desvirt_topologies
[[ -d desvirt_logs ]] || mkdir desvirt_logs

del_prefix="irq_enable + _native_in_isr"
EUSER=$(who am i | awk '{print $1}')

make clean all

for i in 1 5 10 15 20; do
    NODES=$i
    TS=$(date +%s)

    python generate_topology.py ${NODES} > desvirt_topologies/star${NODES}.xml
    chown -R ${EUSER}:${EUSER} desvirt_topologies
    cp -pf desvirt_topologies/star${NODES}.xml RIOT/dist/tools/desvirt/desvirt/.desvirt

    TOPO=star${NODES} make desvirt-define
    TOPO=star${NODES} make desvirt-start

    PORT_ROOT=$(ps au | grep star${NODES}_a1, | grep TCP-L | awk -F, '{  print $4 }' | cut -d\: -f 2)
    echo ${PORT_ROOT}
    echo "ifconfig 6 add abcd::1" | nc localhost ${PORT_ROOT} > /dev/null
    echo "rpl root 1 abcd::1" | nc localhost ${PORT_ROOT} > /dev/null

    for port in $(ps au | grep star${NODES} | grep TCP-L | awk -F, '{ print $4 }' | cut -d\: -f 2); do
        echo ${port}
        nc localhost ${port} | while read l; do
            echo "$(date +%s);${port};$l" | sed -e "s/${del_prefix}//g" | sed "/RPL/!d" | tr -d '> ' >> desvirt_logs/star${NODES}_${port}_${TS}.txt;
        done &
    done

    sleep 60

    TOPO=star${NODES} make desvirt-stop
    TOPO=star${NODES} make desvirt-undefine

    sort -t';' -k1 ./desvirt_logs/star${NODES}*.txt > ./desvirt_logs/log_star${NODES}.txt
    rm -f ./desvirt_logs/star${NODES}*.txt
done

chown -R ${EUSER}:${EUSER} desvirt_logs
