wget https://raw.githubusercontent.com/youzi1984/CS655ProjectFall2020/main/WebServer/package.json
wget https://raw.githubusercontent.com/youzi1984/CS655ProjectFall2020/main/WebServer/package-lock.json
wget https://raw.githubusercontent.com/youzi1984/CS655ProjectFall2020/main/WebServer/404.html
wget https://raw.githubusercontent.com/youzi1984/CS655ProjectFall2020/main/WebServer/status.html
wget https://raw.githubusercontent.com/youzi1984/CS655ProjectFall2020/main/WebServer/index.js


mkdir client
mkdir client/css
mv 404.html client/
mv status.html client/
echo "Download done!"

echo "Setting up environment for web server..."
sudo apt-get update
sudo apt-get install nodejs
sudo apt-get install npm
sudo npm install
echo "Environment (NodeJS) is set up!"

echo "Please run $ node index.js to start!"

