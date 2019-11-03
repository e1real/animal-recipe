FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y default-mysql-client
ADD . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --dev
CMD ["pipenv", "run" ,"./manage.py", "migrate"]