#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

#include "net/af.h"
#include "net/conn/udp.h"
#include "net/ipv6/addr.h"
#include "net/gnrc/rpl.h"
#include "net/gnrc/rpl/dodag.h"
#include "thread.h"

#define SERVER_MSG_QUEUE_SIZE   (8)
#define SERVER_BUFFER_SIZE      (64)

static bool server_running = false;
static conn_udp_t conn;
static char server_buffer[SERVER_BUFFER_SIZE];
static char server_stack[THREAD_STACKSIZE_DEFAULT];
static msg_t server_msg_queue[SERVER_MSG_QUEUE_SIZE];
static char addr_str[IPV6_ADDR_MAX_STR_LEN];

uint64_t time;
bool acked = true;

int udp_send(int argc, char **argv)
{
    if (argc != 4) {
        puts("Usage: udp <ipv6-addr> <port> <payload>");
        return -1;
    }

    int res;
    ipv6_addr_t src = IPV6_ADDR_UNSPECIFIED, dst;
    if (ipv6_addr_from_str(&dst, argv[1]) == NULL) {
        puts("Error: unable to parse destination address");
        return 1;
    }

    if((res = conn_udp_sendto(argv[3], strlen(argv[3]), &src, sizeof(src), &dst, sizeof(dst),
                              AF_INET6, 1234, (uint16_t) (atoi(argv[2])))) < 0) {
        puts("could not send");
    }
    else {
        //printf("Success: send %u byte to %s\n", (unsigned) res, argv[1]);
        if (gnrc_rpl_instances[0].state && gnrc_rpl_instances[0].dodag.node_status != GNRC_RPL_ROOT_NODE) {
            if (acked) {
                time = xtimer_now64();
                acked = false;
            }
        }
    }
    return 0;
}

void *_udp_server(void *args)
{
    uint16_t port = (uint16_t) atoi(args);
    ipv6_addr_t server_addr = IPV6_ADDR_UNSPECIFIED;
    msg_init_queue(server_msg_queue, SERVER_MSG_QUEUE_SIZE);

    if(conn_udp_create(&conn, &server_addr, sizeof(server_addr), AF_INET6, port) < 0) {
        return NULL;
    }

    server_running = true;
    printf("Success: started UDP server on port %" PRIu16 "\n", port);

    char *arg[4];
    char *cmd = "udp_send";
    char *port_str = "8888";

    arg[0] = cmd;
    arg[2] = port_str;
    char src_str[IPV6_ADDR_MAX_STR_LEN];

    while (1) {
        int res;
        ipv6_addr_t src;
        size_t src_len = sizeof(ipv6_addr_t);
        if ((res = conn_udp_recvfrom(&conn, server_buffer, sizeof(server_buffer),
                                     &src, &src_len, &port)) < 0) {
            puts("Error while receiving");
        }
        else if (res == 0) {
            puts("No data received");
        }
        else {
            server_buffer[res] = '\0';
            if (gnrc_rpl_instances[0].state && gnrc_rpl_instances[0].dodag.node_status == GNRC_RPL_ROOT_NODE) {
                printf("%s;%s\n", ipv6_addr_to_str(src_str, &src, sizeof(src_str)),
                                                   server_buffer);
                ipv6_addr_to_str(addr_str, &ipv6_addr_all_nodes_link_local, sizeof(addr_str));
                arg[1] = addr_str;
                arg[3] = src_str;
                udp_send(4, arg);
            }
            else {
                ipv6_addr_t payload;
                ipv6_addr_from_str(&payload, server_buffer);
                if ((gnrc_ipv6_netif_find_by_addr(NULL, &payload) != KERNEL_PID_UNDEF) && (!acked)) {
                    acked = true;
                    printf("diff: %llu\n", xtimer_now64() - time);
                }
            }
        }
    }

    return NULL;
}

int udp_server(int argc, char **argv)
{
    if (argc != 2) {
        puts("Usage: udps <port>");
        return -1;
    }

    if ((server_running == false) &&
        thread_create(server_stack, sizeof(server_stack), THREAD_PRIORITY_MAIN - 2,
                      THREAD_CREATE_STACKTEST, _udp_server, argv[1], "UDP Server")
        <= KERNEL_PID_UNDEF) {
        return -1;
    }

    return 0;
}
