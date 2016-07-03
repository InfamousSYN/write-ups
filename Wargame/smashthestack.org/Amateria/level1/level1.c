#include <stdio.h>
#include <signal.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <syslog.h>
#include <openssl/md5.h>

void flapmud(int lol)
{
        char buf[100];
        syslog(LOG_DEBUG, "Noes :(");
        snprintf(buf, sizeof buf, "/usr/bin/gdb --pid=%d", getpid());
        system(buf);
        exit(1);
}


int main(int argc, char **argv)
{

        int i;

        unsigned char buf[MD5_DIGEST_LENGTH];

        setresuid(geteuid(), geteuid(), geteuid());

        signal(SIGSEGV, flapmud);

        if(argc == 1) { printf("Usage: %s <string>\n", argv[0]); exit(1); }


        MD5(argv[1], strlen(argv[1]), buf);

        for(i = 0; i < MD5_DIGEST_LENGTH; i++) printf("%02x", buf[i]);

        printf(" - %s\n", argv[1]);

        return 0;
}