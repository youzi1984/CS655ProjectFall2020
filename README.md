# CS655ProjectFall2020
## Run password cracker

If you're running the project on nodes that are already reserved by us, please go to Section 2 directly.
Otherwise, start with Section 1 to set up servers on GENI.

### Section 1: Deploy the project on GENI

1. Reserve resources on GENI

   Use the Rspec "password-cracker" to reserve nodes.

2. Set up the web server

   Log into the node with clientID "Webserver" and run the following one by one:

   \$ wget https://raw.githubusercontent.com/youzi1984/CS655ProjectFall2020/main/webserver.sh
   
   \$ chmod +x webserver.sh
   
   \$ ./webserver.sh

3. Set up the job server

   Log into the node with clientID ""

   \$ wget https://raw.githubusercontent.com/youzi1984/CS655ProjectFall2020/main/job-server.py

4. Set up workers

   Log into the nodes with clientID "workerx", where x is number 1 to 10.

   Run the following commands:

   \$ wget https://raw.githubusercontent.com/youzi1984/CS655ProjectFall2020/main/worker.py
   
   
### Section 2: Use the web interface to interact

1.  Run the following commands in order to start the system

    For Webserver: \$ node index.js
    
    For Job Server: \$ python job-server.py
    
    For workers: \$ python worker.py

1.  In a web browser, go to "webserver_ip:9007", where webserver_ip can be found on GENI.

    For our resource, go to http://web-server.passwordcrackerglsz.ch-geni-net.geni.uchicago.edu:9007/
    
2.  Enter md5 hash, number of workers (1-10) and press "submit"
   
    Wait until the result comes back. 
       
 **Important assumptions**
 
 Max number of clients (web interface) at the same time: 1
 
 Max number of worker nodes: 10
 
 Input md5 hash for a 5-character password (a-z, A-Z) must be valid. We use this website for generating md5 hash: https://www.md5hashgenerator.com
