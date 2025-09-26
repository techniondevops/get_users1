FROM python:3.12-slim  
#slim python image

WORKDIR /app 


COPY requirements.txt . 
#copy python directories

RUN pip install -r requirements.txt 
#install python requirements

COPY . . 
CMD ["python","users.py"]

