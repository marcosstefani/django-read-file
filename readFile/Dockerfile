FROM python:3
ENV PYTHONUNBUFFERED=1
COPY . /code/
WORKDIR /code
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]