# syntax=docker/dockerfile:1
FROM python:3.9-alpine
WORKDIR /code
ENV FLASK_APP=cims_ui
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
RUN pip install -e .
CMD ["gunicorn", "wsgi:app", "--preload", "--timeout=420", "--config=gconf.py"]
# Build the image using: docker build --tag <image_name> .
# Once image has been built, run the container via: docker run -it -d -p 5000:5000 <image_name>

#CMD ["flask","run","--host","0.0.0.0"]
