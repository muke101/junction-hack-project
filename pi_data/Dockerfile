FROM balenalib/rpi-raspbian:latest
RUN apt update -y && apt install -y python3 python3-pip
RUN pip3 uninstall numpy && apt install libatlas3-base -y
RUN pip3 install numpy flask flask_restplus requests flask_swagger_ui sqlalchemy pandas flask_swagger
EXPOSE 31999
ADD . /
CMD ["python3.7","./app.py"]

