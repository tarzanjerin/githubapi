FROM python:alpine3.16
WORKDIR /data
RUN pip install requests argparse datetime timedelta
COPY api.py /data
ENTRYPOINT ["python", "api.py"]