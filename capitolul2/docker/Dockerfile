FROM kalilinux/kali-rolling

LABEL org.opencontainers.image.authors="Sergiu Nisioi <sergiu.nisioi@fmi.unibuc.ro>"

USER root

RUN apt-get update && apt-get install -y build-essential git net-tools arp-scan python3 python3-pip tcpdump ethtool nmap rtpflood traceroute

RUN pip3 install --break-system-packages cryptography notebook bs4 "connexion[swagger-ui]" flask

RUN git clone https://github.com/senisioi/scapy.git && cd scapy && python3 setup.py install

RUN apt-get update && apt-get install -y iputils-ping dnsutils

RUN apt-get update && apt-get install -y curl

RUN apt-get update && apt-get install -y openssh-server

RUN mkdir -p /var/run/sshd

RUN echo 'root:root' | chpasswd

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
