FROM balenalib/rpi-raspbian:latest
RUN apt update -y && apt install -y python3 python3-pip
RUN pip3 install flask flask_restplus requests flask_swagger_ui
EXPOSE 31999

