# Devops Labs 1 & 2
## Asanali Fazylzhan. SE-01
## Installation
1. Clone repository<br/>
`git clone https://github.com/Asanali12/devops.git`
2. Install `pdm` for managing packages<br/>
`cd app_python
pip install pdm==1.8.0`
3. Install all needed dependencies<br/>
`pdm install`
## Run
1. To run use `pdm`<br/>
`pdm run python app.py`<br/>
Access application in browser via address displayed in terminal.
## Docker
- Build locally <br/>
`docker build . -t asanali99/devops_lab1`
- Pull docker image from DockerHub<br/>
`sudo docker pull asanali99/devops_lab1:latest`
- Run<br/>
`docker run -p 5000:5000 asanali99/devops_lab1:latest`
