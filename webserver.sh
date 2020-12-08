wget https://raw.githubusercontent.com/Zhongping-Zhang/CS655-mini-project/main/src/Web%2BWebServer/package.json
wget https://raw.githubusercontent.com/Zhongping-Zhang/CS655-mini-project/main/src/Web%2BWebServer/package-lock.json
wget https://raw.githubusercontent.com/Zhongping-Zhang/CS655-mini-project/main/src/Web%2BWebServer/client/404.html
wget https://raw.githubusercontent.com/Zhongping-Zhang/CS655-mini-project/main/src/Web%2BWebServer/client/status.html
wget https://raw.githubusercontent.com/Zhongping-Zhang/CS655-mini-project/main/src/Web%2BWebServer/index.js


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

