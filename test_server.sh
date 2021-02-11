#!/bin/bash
chmod +x install.sh
sudo ./install.sh
chmod +x server_run.sh
./server_run.sh &
chmod +x sleep.sh
./sleep.sh
curl --location --request GET http://localhost:8081/memes
curl --location --request POST http://localhost:8081/memes --header Content-Type:application/json --data-raw "{\"name\":\"Hello testing\",  \"url\":\"https://i.ytimg.com/vi/if-2M3K1tqk/maxresdefault.jpg\",  \"caption\":\"This is a testing meme\"}"
curl --location --request GET http://localhost:8081/memes
curl --location --request GET http://localhost:8081/swagger-ui/