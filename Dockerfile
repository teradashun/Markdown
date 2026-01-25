FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY my_scraper.py /app/

CMD ["bash"]