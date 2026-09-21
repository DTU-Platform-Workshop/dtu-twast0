FROM python:3.12-slim

ENV PYTHONBUFFERED=1 \
    PORT=4242 \
    HOME=/tmp \
    TMPDIR=/tmp

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app/

USER 10001

EXPOSE 4242

ENTRYPOINT ["python"]

CMD ["app.py"]