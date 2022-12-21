FROM python:3.9
COPY requirements.txt /app/requirements.txt
WORKDIR /app
ADD . /app/data
COPY ./data/output.json ./app/data
RUN ls
RUN pip install --no-cache-dir -r requirements.txt
COPY get_results.py ./