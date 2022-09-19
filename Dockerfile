FROM python:3.8

WORKDIR /techtrends

COPY ./techtrends ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3111

CMD [ "python", "app.py" ]