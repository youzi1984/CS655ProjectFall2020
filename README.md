# CS655ProjectFall2020
## Run password cracker

If you're running the project on nodes that are already reserved and configured by us, then please go to Section 2 directly.
Otherwise, start with Section 1 to set up servers on GENI.

### Section 1: Deploying the project on GENI

1. Reserve resources on GENI

   Use the Rspec "resources.rspec" to reserve the resources on GENI.

2. Set up the web-server

   Log into the "web-server" node and run the following one by one to configure the node:

   \$ wget https://raw.githubusercontent.com/youzi1984/CS655ProjectFall2020/main/webserver.sh
   
   \$ chmod +x webserver.sh
   
   \$ ./webserver.sh

3. Set up the jobs-server

   Log into the "jobs-server" node and run the following command to retrieve the code that needs to run on it:

   \$ wget https://raw.githubusercontent.com/youzi1984/CS655ProjectFall2020/main/job-server.py

4. Set up the worker nodes

   Log into the nodes name "worker-x", where x is number 1 to 10.

   Run the following command on each to retrieve the code that needs to run on it:

   \$ wget https://raw.githubusercontent.com/youzi1984/CS655ProjectFall2020/main/worker.py
   
   
### Section 2: Using the web interface to interact with the system
Note: Make sure to do the following in this precise order.

1.  Run the following commands in order to start the system, running each on their respective nodes:
    
    For the jobs-server: \$ python job-server.py
    
    For the web-server: \$ node index.js

2.  In a web browser, go to "webserver_ip:9007", where webserver_ip can be found on GENI.

    If you're using our GENI resources, go to http://web-server.passwordcrackerglsz.ch-geni-net.geni.uchicago.edu:9007/
    
3.  Enter the md5 hash belonging to the 5 letter password with alphabet (a-z, A-Z).
    
    Select the number of workers (1-10) with the arrow on the right (do not enter directly).
    
    press "submit"
   
    Wait until the result comes back. 
    
4. For each of the workers, run the following command: \$ python worker.py

   When all workers are connected to the jobs-server, they will receive a message notifying you that the system is ready to go, and it will automatically start to figure out what the password is from the client.
    

       
 **Important assumptions**
 
 Max number of clients (web interface) at the same time: 1
 
 Max number of worker nodes: 10
 
 The input md5 hash for the 5-character password (a-z, A-Z) must be valid. We used this website for generating the md5 hash: https://www.md5hashgenerator.com.
