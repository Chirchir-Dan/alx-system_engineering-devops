#0x0D. Web Stack Debugging #0
##Description
This project involves debugging an Apache server running inside a Docker container. The goal is to ensure the server returns a page containing "Hello Holberton" when querying the root of the container.

##Requirements
Docker installed on your local machine.
Basic understanding of Docker and containerization.
Basic knowledge of Apache server configuration.

##Task
##0. Give Me a Page!
In this first debugging task, you will get Apache to run on the container and return a page containing "Hello Holberton" when querying the root.

###Steps to Complete the Task
###Run the Docker Container:

Run the Docker container using the following command:

docker run -p 8080:80 -d -it holbertonschool/265-0

###Verify the Running Container:

Check if the container is running:
docker ps

You should see output similar to this:

CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
47ca3994a491        holbertonschool/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp   vigilant_tesla
###Test the Server Response:

Query port 8080 on your local machine:
curl 0:8080

If you receive an error message like curl: (52) Empty reply from server, proceed to debug the issue.

###Debug the Container:

Connect to the running container:
docker exec -it <container_id> /bin/bash
Replace <container_id> with the actual container ID from the docker ps output.

#Start Apache Server:

If Apache is not running, start it:
service apache2 start

###Verify the Fix:

Exit the container and run the curl command again:
curl 0:8080
You should see the output:

Hello Holberton

##Example Commands to Fix the Issue:
docker exec -it <container_id> /bin/bash
service apache2 start
exit
curl 0:8080

##Additional Information
For more details on Docker and containerization, refer to the Docker documentation.

##Author
Chirchir-Dan - GitHub Profile
