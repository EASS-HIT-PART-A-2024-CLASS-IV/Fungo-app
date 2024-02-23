FROM python:3.11

COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt

EXPOSE 6699

CMD ["uvicorn", "db_server_main:app" , "--host", "0.0.0.0", "--port", "6699", "--reload"]