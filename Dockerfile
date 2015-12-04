FROM python:3.5

ENV REPO /repo
ENV PYTHONPATH ${REPO}

WORKDIR ${REPO}

COPY . ${REPO}

RUN pip install -r requirements.txt

CMD ./manage.py runserver 0.0.0.0:8000
