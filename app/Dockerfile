FROM python:3.6

WORKDIR /usr/src/app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install apt-utils -y
RUN apt-get install sqlite3 -y

COPY . .

RUN pip install flask
RUN pip freeze > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "python3", "./demo.py" ]