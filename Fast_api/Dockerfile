FROM python:3.8.10
COPY . /main
WORKDIR /main
RUN pip install -r requirements.txt
CMD ["uvicorn","main:app"]
