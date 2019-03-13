# Use an official ubuntu runtime as a parent image
FROM ubuntu:18.04

# Set container working directory to /
WORKDIR /

# Copy everything in current directory into the container at /
COPY . /

# Install the requied packages for packages related with odbc, python, and clean while finish
RUN apt-get update \
&& apt-get -y install curl \
&& apt-get -y install gnupg gnupg1 gnupg2 gcc  \
&& curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list  \
&& curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  \
&& apt-get update  \
&& apt-get install -y libssl1.0.0 \
&& ACCEPT_EULA=Y apt-get install -y  msodbcsql17 \
&& ACCEPT_EULA=Y apt-get install -y mssql-tools \
&& ACCEPT_EULA=Y apt-get install -y unixodbc-dev \
&& apt-get -y install python3.6 \
&& apt-get -y install python3-pip \
&& pip3 install -r pip3package.txt \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* \
&& rm -rf /tmp/*
