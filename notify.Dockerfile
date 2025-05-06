FROM python:3.14.0a6-alpine
COPY notify.py ./
RUN pip install requests
CMD sh -c "python notify.py"