FROM python:3.9
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 3000
CMD ["python", "manage.py", "runserver", "3000"]