APPLICATION = unreachability_time
BOARD ?= native
RIOTBASE ?= $(CURDIR)/RIOT

USEMODULE += gnrc_netdev_default
USEMODULE += auto_init_gnrc_netif
USEMODULE += gnrc_ipv6_router_default
USEMODULE += gnrc_udp
USEMODULE += gnrc_rpl
USEMODULE += gnrc_rpl_unicast_checks
USEMODULE += gnrc_ipv6_blacklist
USEMODULE += auto_init_gnrc_rpl
USEMODULE += gnrc_conn_udp
USEMODULE += gnrc_icmpv6_echo
USEMODULE += shell
USEMODULE += shell_commands
USEMODULE += ps


CFLAGS += -DDEVELHELP
CFLAGS += -DGNRC_RPL_PARENTS_NUMOF=3
CFLAGS += -DGNRC_PKTBUF_SIZE=4096
CFLAGS += -DGNRC_IPV6_NC_SIZE=32
CFLAGS += -DGNRC_RPL_MSG_QUEUE_SIZE=32
CFLAGS += -DGNRC_IPV6_MSG_QUEUE_SIZE=32
CFLAGS += -DGNRC_RPL_BLOOM_SIZE=32
CFLAGS += -DGNRC_RPL_BLACKLIST_BLOOM_SIZE=32

QUIET ?= 1

include $(RIOTBASE)/Makefile.include
