FROM selenium/standalone-chrome:latest

WORKDIR /app

COPY firsttest.py .

RUN pip install selenium

CMD ["python3", "firsttest.py"]
