FROM python:3.12-slim

ENV DB_HOST=${DB_HOST}
ENV DB_PORT=${DB_PORT}
ENV DB_NAME=${DB_NAME}
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}

WORKDIR /app

COPY requirements requirements
RUN pip install -r requirements/requirements.txt

COPY . .

RUN chmod +x start.sh
CMD ["./start.sh"]
