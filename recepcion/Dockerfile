FROM python:3.9

ENV DASH_DEBUG_MODE True
COPY ./recepcion/requirements.txt /recepcion/requirements.txt
COPY ./recepcion/recepcion.py /recepcion/recepcion.py
WORKDIR /recepcion
RUN set -ex && \
    pip install -r requirements.txt
EXPOSE 8051
EXPOSE 3002
CMD ["python", "recepcion.py"]
