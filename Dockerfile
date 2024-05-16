# Pull base image
FROM python:3.12.3-slim

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV POETRY_VERSION=1.8.3
ENV POETRY_NO_INTERACTION=1


# System dependencies
RUN pip install poetry==$POETRY_VERSION

# Set work directory
WORKDIR /resizinator

# Install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false --local
RUN poetry install

# Copy project
COPY . .
