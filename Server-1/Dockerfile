FROM python:3.9

WORKDIR /Server-1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . . 
CMD ["python", "app.py"]