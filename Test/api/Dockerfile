FROM python:3

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY api/requirement.txt requirement.txt
RUN pip install --upgrade pip
RUN pip install -r requirement.txt
COPY api /app
EXPOSE 8000