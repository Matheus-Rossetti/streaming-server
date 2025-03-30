FROM python

WORKDIR /streaming-server

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [flask run]