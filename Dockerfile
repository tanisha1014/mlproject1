 FROM python:3.9-slim-buster  
 ##it will fetch everything from the docker hub(repository)if we want or want to fetch anything
#fetching image from the docker hub
WORKDIR /service
COPY requirements.txt .
COPY . ./     
##copy current dir to wor dir
RUN pip install -r requirements.txt
ENTRYPOINT ["python3","app.py"]