FROM python:3.9 as python-base

RUN mkdir ai_piping

WORKDIR  /ai_piping

COPY . .
RUN pip install -r requirements.txt

CMD pip3 list

ENTRYPOINT ["sh", "entrypoint.sh"]