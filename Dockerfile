FROM python:3.8

RUN pip3 install spacy-2.3.2
RUN pip3 install "https://github.com/megagonlabs/ginza/releases/download/latest/ginza-latest.tar.gz"
