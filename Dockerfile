FROM python:3.8.10

# Exposing port
EXPOSE 8000

# Environment Variables
ENV SQLALCHEMY_DATABASE_URL "sqlite:///./brahat_mrdanga.db"

# Copying source code
COPY ./requirements.txt /brahat-mrdanga/
COPY ./src/ /brahat-mrdanga/src

# Installing dependencies
RUN pip install -r /brahat-mrdanga/requirements.txt

# Setting working directory
WORKDIR /brahat-mrdanga/src

# Running application
CMD ["python", "main.py"]
