FROM python:3.8.10
COPY . /test
WORKDIR /test
RUN pip install -r requirements.txt
CMD ["python","main.py"]