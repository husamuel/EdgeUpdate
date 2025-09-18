FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir Flask==2.3.2 requests prometheus_client
CMD ["python", "device.py"]
EXPOSE 5000