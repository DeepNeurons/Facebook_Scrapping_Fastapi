# Facebook_Scrapping_Fastapi
### Package installation
`pip install fastapi uvicorn facebook-scraper pymongo`
## test locally 
`uvicorn main:app --reload`
### test container
`docker exec -it <container name> <command>`
### potential problems:
1. permession denied while trying to connect to docker daemon use this command below
`sudo chmod 666/var/run/docker.sock`
2. listening port not available (for the mongodb)
in terminal : `sudo lsof -i tcp:27017` to check in use ports
