FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN rm -f *.db
RUN rm -R -f */__pycache__
RUN rm -R -f __pycache__

EXPOSE 8000

ENTRYPOINT [ "uvicorn", "app:app", "--host=0.0.0.0"]