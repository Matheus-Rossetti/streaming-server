FROM python

WORKDIR /streaming-server

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["flask", "run"]