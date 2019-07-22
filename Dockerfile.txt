FROM python:3.6-onbuild
RUN mkdir /Recommendation-systems
COPY . /Recommendation-systems
WORKDIR /Recommendation-systems
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_ENV="docker"
EXPOSE 8000
