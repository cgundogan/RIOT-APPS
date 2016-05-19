APPLICATION = netstats_printer
BOARD ?= native
RIOTBASE ?= $(CURDIR)/RIOT

USEMODULE += gnrc_netdev_default
USEMODULE += auto_init_gnrc_netif
USEMODULE += gnrc_ipv6_router_default
USEMODULE += gnrc_udp
#USEMODULE += gnrc_rpl_bloom
USEMODULE += gnrc_rpl
USEMODULE += gnrc_rpl_unicast_checks
USEMODULE += auto_init_gnrc_rpl
USEMODULE += netstats_rpl
USEMODULE += gnrc_pktdump
USEMODULE += gnrc_icmpv6_echo
USEMODULE += shell
USEMODULE += shell_commands
USEMODULE += ps

CFLAGS += -DDEVELHELP
CFLAGS += -DGNRC_RPL_PARENTS_NUMOF=5

QUIET ?= 1

include $(RIOTBASE)/Makefile.include
