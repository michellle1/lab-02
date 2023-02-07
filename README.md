# Lab 2
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Michelle Arredondo
- Nayeli De Leon

## Lab Question Answers

1. What is argc and *argv[]?
	argc is an integer value. *argv[] is a pointer to an array. 
	
2. What is a UNIX file descriptor and file descriptor table?
	UNIX file descriptor is an unsigned integer that a procress uses to identify an open file. A file descriptor table consists of a set of pointers to an open file structure. The file descriptor is an index to this table of pointers.
	SOURCES:
	-https://www.ibm.com/docs/en/aix/7.1?topic=volumes-using-filedescriptors 
	-https://amine2019.medium.com/file-descriptors-file-descriptortables-and-file-structures-4805d46d176c 
	
3. What is a struct? What's the structure of sockaddr_in?
	A struct groups related variables in one place, where each variable is a member of the structure. A struct can contain different types of variables.
	source: https://www.w3schools.com/c/c_structs.php 
	
	sockaddr_in contains two variables for the socket address and the client address. 

4. What are the input parameters and return value of socket()
	The input parameters of socket() are 'AF_INET' which is the communications domain in which the socket will be created, 'SOCK_STREAM' which is the type of socket that will be created, and '0' which is the specific protocol that the socket will use. '0' protocol will allow the socket to use the appropriate default protocol. socket() returns a file descriptor which is represented by the variblae 'sockfd' in the tcp_server code. 
	source: https://pubs.opengroup.org/onlinepubs/009604499/functions/socket.html

5. What are the input parameters of bind() and listen()?
	The input parameters of bind() are the file descriptor for the socket, a pointer to the structure that contains the socket address with a reference to said socket address, and the length of the structure.
	source: https://pubs.opengroup.org/onlinepubs/009695399/functions/bind.html 
	
	The input parameters of listen() are the socket file descriptor and a backlog variable of type int. The backlog acts like a queue for incoming connection requests. 
	source: https://www.ibm.com/docs/en/zos/2.4.0?topic=functions-listen-prepare-server-incoming-client-requests

6. Why use while(1)? Based on the code below, what problems might occur if there are multiple simultaneous connections to handle?

	while(1) will repeat the loop forever until the program is stopped. You could probably get an error if there are multiple simultaneous connections because the program only accepts one client socket, which is represented by 'newsockfd'. 

7. Research how the command fork() works. How can it be applied here to better handle multiple connections?

	fork() is a system call that can create a new process, which is called a child process, and run the child process at the same time as the parent process. Both the parent and child processes will execute the next line instruction after the fork() system call. This could be applied to better handle multiple connections by allowing the program to create multiple file descriptors for new client sockets and run the same process of the server reading and writing to the client for each client connection. 
	
	source: https://www.geeksforgeeks.org/fork-system-call/ 

8. This program makes several system calls such as 'bind', and 'listen.' What exactly is a system call?
	A system call is a way for a computer program to request a service from the kernel of the operating system. 
	source: https://www.geeksforgeeks.org/introduction-of-system-call/ 
