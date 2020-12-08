var os = require("os");
// include the express module
var express = require("express");
// create an express application
var app = express();
// helps in extracting the body portion of an incoming request stream
var bodyparser = require('body-parser');
// fs module - provides an API for interacting with the file system
var fs = require("fs");
// helps in managing user sessions
var session = require('express-session');
// native js function for hashing messages with the SHA-256 algorithm
var crypto = require('crypto');

var net = require('net');


var nodelist; // hold all worker nodes
var nodeworks = {};

UserID = 0;
UserDB = new Map();



// apply the body-parser middleware to all incoming requests
app.use(bodyparser());

// use express-session
// in memory session is sufficient for this assignment
app.use(session({
  secret: "CS655GENIProj",
  saveUninitialized: true,
  resave: false}
));

// server listens on port 9007 for incoming connections
app.listen(9007, () => {
  console.log("Start Web server successfully!");
  console.log("=======================");
  console.log("Listening port: 9007");
  console.log("Access URL: " + require('os').hostname() + ":9007");
  console.log("=======================");});


var hostname = os.hostname();


// GET method to return the status
// The function queries the table events for the list of places and sends the response back to client
//post: submit data to specified resources
//get: fetch data from specified resource
app.get('/', function(req, res) {
  req.session.value=UserID;
  UserDB.set(req.session.value, new Map());
  UserID = UserID+1;
  res.sendFile(__dirname+'/client/status.html');
});

//client = new net.Socket();
app.post('/getProgess', function(req, res) { 
  if (req.session.value) {
    console.log(req.body.Hashed_MD5);
    // client = UserDB.get(req.session.value).get("Working");
    // if(client){
    //  var formData = {
    //      'Password'              : "dup req"
    //  };
    //  console.log("dup req!!!")
    //  return;
    //}
    UserDB.set(req.session.value, UserDB.get(req.session.value).set("working", true));
    client = new net.Socket();
  
    console.log("start======>>")
    client.connect(9007, '172.17.2.13', function() {
	console.log('Connected');
    	client.write(""+req.body.Hashed_MD5+"\t"+req.body.Number_of_Node+"\n"); 
		// *********** send data to jobs-server ************
    });
    UserDB.set(req.session.value, UserDB.get(req.session.value).set("Cs", client));
    UserDB.set(req.session.value, UserDB.get(req.session.value).set("nodecount", req.body.Number_of_Node));

    client.on('data', function(data) {
      console.log(data.toString());
      var formData = {
          'Password'              : data.toString()
      };
       console.log("output===========>>>");
       //res.write(JSON.stringify(formData));
       res.send(JSON.stringify(formData));
       console.log("DEBUG");
    });
    UserDB.set(req.session.value, UserDB.get(req.session.value).set("working", false));
  } else {
    console.log("new job");
    res.redirect('/');
  }
});


/* app.post('/reConfigPartitionSize', function(req, res) {
  console.log("in reConfigPartitionSize");
  console.log(req.session.value);
  if (req.session.value) {
    // console.log(req.body.Hashed_MD5);
    client = UserDB.get(req.session.value).get("Cs");
    if(client){
      // client.connect(1337, 'localhost', function() {
      	// console.log('Connected');
      	client.write("p/"+req.body.Size_of_Partition+"\n");
        UserDB.set(req.session.value, UserDB.get(req.session.value).set("partitionsize", req.body.Size_of_Partition));
      // });

    } else {
    }
    res.end("done");
    // client.on('close', function() {
    // 	console.log('Connection closed');
    // });
  } else {
    console.log("new job");
    res.redirect('/');
  }
});
 */
 
app.post('/reConfigNumberOfNode', function(req, res) {
  console.log("in reConfigNumberOfNode");
  console.log(req.session.value);
  if (req.session.value) {
    client = UserDB.get(req.session.value).get("Cs");
    if(client) {
      console.log("n/"+req.body.Number_of_Node+"\n");
      client.write("n/"+req.body.Number_of_Node+"\n");
      UserDB.set(req.session.value, UserDB.get(req.session.value).set("nodecount", req.body.Number_of_Node));

    } else {
    }
    res.end("done");
  } else {
    console.log("new job");
    res.redirect('/');
  }
});


// middle ware to serve static files
app.use('/client', express.static(__dirname + '/client'));


// function to return the 404 message and error to client
app.get('*', function(req, res) {
  // add details
  res.sendFile(__dirname+'/client/404.html');
});

