#include <stdio.h>
#include <string.h>

#include "msg.h"
#include "shell.h"
#include "thread.h"
#include "net/gnrc/rpl.h"
#include "net/gnrc/rpl/dodag.h"

#define MAIN_QUEUE_SIZE     (8)
static msg_t _main_msg_queue[MAIN_QUEUE_SIZE];
static msg_t _send_msg_queue[MAIN_QUEUE_SIZE];

extern int udp_send(int argc, char **argv);
extern int udp_server(int argc, char **argv);

static char _stack[THREAD_STACKSIZE_DEFAULT];

static const shell_command_t shell_commands[] = {
    { "udp", "send udp packets", udp_send },
    { "udps", "start udp server", udp_server },
    { NULL, NULL, NULL }
};

void *_send(void *args)
{
    (void) args;
    msg_init_queue(_send_msg_queue, MAIN_QUEUE_SIZE);

    char *arg[4];
    char *cmd = "udp_send";
    char *dst = "abcd::1";
    char *port = "8888";
    char rank[12];

    arg[0] = cmd;
    arg[1] = dst;
    arg[2] = port;

    while(1) {
        xtimer_sleep(2);
        if (gnrc_rpl_instances[0].state && gnrc_rpl_instances[0].dodag.my_rank == GNRC_RPL_ROOT_RANK) {
            return NULL;
        }

        if (gnrc_rpl_instances[0].state) {
            memset(rank, 0, sizeof(rank));
            sprintf(rank, "%u", gnrc_rpl_instances[0].dodag.my_rank);
            arg[3] = rank;
            udp_send(4, arg);
        }
    }
    return NULL;
}

int main(void)
{
    char *args[2];
    char *cmd = "udp_server";
    char *port = "8888";

    args[0] = cmd;
    args[1] = port;

    msg_init_queue(_main_msg_queue, MAIN_QUEUE_SIZE);

    udp_server(2, args);

    thread_create(_stack, sizeof(_stack), THREAD_PRIORITY_MAIN - 1, THREAD_CREATE_STACKTEST,
                  _send, NULL, "send");

    char line_buf[SHELL_DEFAULT_BUFSIZE];
    shell_run(shell_commands, line_buf, SHELL_DEFAULT_BUFSIZE);

    return 0;
}
