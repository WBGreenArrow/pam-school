FROM python:3.7 AS development

ENV PYTHONUNBUFFERD=1

WORKDIR /usr/src/app

COPY requirements.txt .

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]


