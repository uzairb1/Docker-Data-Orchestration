FROM python:3.9
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
COPY ./data/people.csv ./
COPY ./data/places.csv ./
COPY load_data.py ./