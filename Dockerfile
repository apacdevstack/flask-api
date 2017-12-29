FROM python:2.7-alpine
RUN mkdir -p /app
WORKDIR /app

# Copy dependency files
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy required files
COPY apiapp/ /app/apiapp/
COPY app.py requirements.txt setup.py setup.cfg /app/

EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "-w", "4", "app"]
