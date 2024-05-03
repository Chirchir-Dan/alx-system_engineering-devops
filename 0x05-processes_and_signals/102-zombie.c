#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while -Creates an infinite loop
 *
 * Return: Always returns 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point of the program
 *
 * Return: Always returns 0.
 */
int main(void)
{
	int i;
	pid_t child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == -1)
		{
			perror("fork failed");
			exit(EXIT_FAILURE);
		}
		if (child_pid == 0)
		{
			/* Child process */
			printf("Zombie process created, PID: %d\n", getpid());
			exit(EXIT_SUCCESS);
		}
	}

	/* Parent process */
	infinite_while();
	return (0);
}
