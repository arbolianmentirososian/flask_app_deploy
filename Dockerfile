FROM python:3

RUN useradd -m python

WORKDIR /opt/flask_app_deploy
COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY . .

RUN chown -R python:python /opt/flask_app_deploy

USER python

RUN chmod u+x run.sh

EXPOSE 8080

CMD ["./run.sh"]
