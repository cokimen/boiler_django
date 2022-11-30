FROM python:3.8.10
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 3000
CMD ["./manage.py", "runserver"]


