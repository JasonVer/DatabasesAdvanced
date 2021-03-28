# DatabasesAdvanced

<h1> Web scraping python script </h1>
<h1> part 1</h1>
<h2>script: scraper.py</h2>
<h2> Intro </h2>
The website we used to scrape: https://www.blockchain.com/btc/unconfirmed-transactions <br>
The script will put the scraped variables in two log files, highest.log and all.log <br>

<h2> Requirements </h2>
You need to run python to make use of this script. <br>
If you don't have python installed on your computer, you can simply install python with the help of a youtube tutorial. <br>
I do reccomend to use the latest version of Python (3.9.0). <br>
You need to install pandas and bs4, otherwise the script won't run. <br>
You can do so simply by using following lines: <br>
<ul>
  <li> pip install pandas </li>
  <li> pip install bs4 </li>
</ul>

<h2> Usage </h2>
If you are on a Ubuntu OS you can use the command git clone to download this repository. <br>
<ul>
  <li> link to clone the git: https://github.com/JasonVer/DatabasesAdvanced.git </li>
</ul>
To execute the script use: python3 scraper.py <br>
To stop running the script, type ctrl + c. in the terminal <br>

<h1>part 2</h1>
<h2> script: mongoP.py </h2>
here I will explain how we put data into MongoDB
<h3>script</h3>
First we will change our script a little. in order to make it work we need an extension.
<ul>
  <li> pip install pandas </li>
 </ul>
 
 We still use the Ubuntu VM.
 make sure you updated your git on the VM.
 <h3>MongoDB</h3>
 to make everything work in your VM you need to install MongoDB. We will do this with the following commands.
 <ul>
 <li>sudo apt install curl</li>
<li>curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -</li>
<li>echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list</li>
<li>sudo apt update</li>
<li>sudo apt install mongodb-org</li>
<li>sudo systemctl start mongod.service</li>
<li>sudo systemctl status mongod</li>
<li>sudo systemctl enable mongod</li>
<li>mongo --eval 'db.runCommand({ connectionStatus: 1 })'</li>
</ul>

If you did that you can now work with MongoP.py.

<h1> part 3</h1>
<h2> add Redis to the script</h2>
to install Redis you can follow redis.sh. if you did that, Redis is ready to go.
To put Redis into your script you have to install the feature.
This can you do with: Pip install redis.

<h1> part 4</h1>
in this part we pulled redis and mongo from dockerhub. You can find the both commands in dockerhub.

<h1> part 5</h1>
In the final part we putted the scripts in a container. you can get the container I made on this site: https://hub.docker.com/repository/docker/jasonver/databases-advanced-r0781387
