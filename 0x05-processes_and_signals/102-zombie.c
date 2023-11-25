#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
int infinite_while(void);

/**
* main - Entry point
* Return: int
*/

int main(void)
{
	int i;

	pid_t zombie_pid;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();
		if (!zombie_pid)
		{
			return (0);
		}

		printf("Zombie process created, PID: %d\n", zombie_pid);


	}

	infinite_while();
	return (0);
}

/**
* infinite_while - Function that runs an infinite loop
* Return: 0 (never actually reached)
*/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
