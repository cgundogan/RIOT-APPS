/*
 * Copyright (C) 2015 Freie Universität Berlin
 *
 * This file is subject to the terms and conditions of the GNU Lesser
 * General Public License v2.1. See the file LICENSE in the top level
 * directory for more details.
 */

/**
 * @ingroup     examples
 * @{
 *
 * @file
 * @brief       Example application for demonstrating the RIOT network stack
 *
 * @author      Hauke Petersen <hauke.petersen@fu-berlin.de>
 *
 * @}
 */

#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

#include "shell.h"
#include "msg.h"
#include "random.h"
#include "thread.h"
#include "xtimer.h"
#include "net/netstats.h"
#include "net/gnrc/rpl.h"

#define PRIO                (THREAD_PRIORITY_MAIN - 1)
#define STATS_INTERVAL      (SEC_IN_USEC * 5)
#define MAIN_QUEUE_SIZE     (8)
static msg_t _main_msg_queue[MAIN_QUEUE_SIZE];

static char stats_stack[THREAD_STACKSIZE_DEFAULT];

extern int udp_cmd(int argc, char **argv);

static kernel_pid_t _stats_pid = KERNEL_PID_UNDEF;
static bool print_stats = false;
static netstats_rpl_t *rps = &gnrc_rpl_instances[0].stats;

void *_stats_print(void *arg)
{
    (void) arg;
    while (1) {
        if (print_stats) {
            printf("RPL;%u"
                   ",%"PRIu32",%"PRIu32",%"PRIu32",%"PRIu32
                   ",%"PRIu32",%"PRIu32",%"PRIu32",%"PRIu32
                   ",%"PRIu32",%"PRIu32",%"PRIu32",%"PRIu32
                   ",%"PRIu32",%"PRIu32",%"PRIu32",%"PRIu32
                   ",%"PRIu32",%"PRIu32",%"PRIu32",%"PRIu32
                   ",%"PRIu32",%"PRIu32",%"PRIu32",%"PRIu32
                   ",%"PRIu32",%"PRIu32",%"PRIu32",%"PRIu32
                   ",%"PRIu32",%"PRIu32",%"PRIu32",%"PRIu32
                   "\n",
                   gnrc_rpl_instances[0].dodag.my_rank,
                   rps->dio_rx_ucast_count, rps->dio_rx_ucast_bytes, rps->dio_rx_mcast_count, rps->dio_rx_mcast_bytes,
                   rps->dio_tx_ucast_count, rps->dio_tx_ucast_bytes, rps->dio_tx_mcast_count, rps->dio_tx_mcast_bytes,
                   rps->dis_rx_ucast_count, rps->dis_rx_ucast_bytes, rps->dis_rx_mcast_count, rps->dis_rx_mcast_bytes,
                   rps->dis_tx_ucast_count, rps->dis_tx_ucast_bytes, rps->dis_tx_mcast_count, rps->dis_tx_mcast_bytes,
                   rps->dao_rx_ucast_count, rps->dao_rx_ucast_bytes, rps->dao_rx_mcast_count, rps->dao_rx_mcast_bytes,
                   rps->dao_tx_ucast_count, rps->dao_tx_ucast_bytes, rps->dao_tx_mcast_count, rps->dao_tx_mcast_bytes,
                   rps->dao_ack_rx_ucast_count, rps->dao_ack_rx_ucast_bytes, rps->dao_ack_rx_mcast_count, rps->dao_ack_rx_mcast_bytes,
                   rps->dao_ack_tx_ucast_count, rps->dao_ack_tx_ucast_bytes, rps->dao_ack_tx_mcast_count, rps->dao_ack_tx_mcast_bytes
                  );
        }
        xtimer_usleep(STATS_INTERVAL);
    }
    return NULL;
}

int _stats_cmd(int argc, char **argv)
{
    if (argc != 2) {
        puts("Usage: stats [start|stop]");
        return 1;
    }

    if (strcmp(argv[1], "start") == 0) {
        if (_stats_pid == KERNEL_PID_UNDEF) {
            _stats_pid = thread_create(stats_stack, sizeof(stats_stack), PRIO,
                                       THREAD_CREATE_STACKTEST, _stats_print, NULL, "stats");
        }
        print_stats = true;
    }
    else if (strcmp(argv[1], "stop") == 0) {
        print_stats = false;
    }
    else {
        return 1;
    }

    return 0;
}

static const shell_command_t shell_commands[] = {
    { "stats", "start / stop stats printing", _stats_cmd},
    { "udp", "send data over UDP and listen on UDP ports", udp_cmd },
    { NULL, NULL, NULL }
};

int main(void)
{
    /* we need a message queue for the thread running the shell in order to
     * receive potentially fast incoming networking packets */
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    random_init((uint32_t)ts.tv_nsec);
    msg_init_queue(_main_msg_queue, MAIN_QUEUE_SIZE);
    puts("RIOT network stack example application");

    gnrc_rpl_init(6);

    /* start shell */
    puts("All up, running the shell now");
    char line_buf[SHELL_DEFAULT_BUFSIZE];
    char *arg[2];
    char *cmd = "stats";
    char *status = "start";
    arg[0] = cmd;
    arg[1] = status;
    _stats_cmd(2, arg);

    shell_run(shell_commands, line_buf, SHELL_DEFAULT_BUFSIZE);

    /* should be never reached */
    return 0;
}
