# Use the offical Centos7 image
FROM centos

MAINTAINER Rob Waller <rdwaller1984@googlemail.com>

# Set the working directory
WORKDIR /var/www/html

# Copy local code to app directory
COPY . app

# Setup Centos to run Python 3.6, upgrade pip and install requirements
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm
RUN yum update -y
RUN yum --enablerepo=extras install -y epel-release
RUN yum install -y wget unzip zip git python36u python36u-pip
RUN rm /usr/bin/python
RUN ln -s /usr/bin/python3.6 /usr/bin/python
RUN python -m pip install --upgrade pip
RUN python -m pip install --trusted-host pypi.python.org -r app/requirements.txt

# Make port 5000 available for flask
EXPOSE 5000

# Define environment variables so flask works
ENV LANG en_US.UTF-8
ENV FLASK_APP app/main.py

# Run flask
CMD python -m flask run --host=0.0.0.0
