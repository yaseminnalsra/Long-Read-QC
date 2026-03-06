FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    gcc g++ zlib1g-dev libbz2-dev \
    libncurses5-dev liblzma-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    biopython==1.81 \
    pandas==2.0.3 \
    matplotlib==3.7.2 \
    seaborn==0.12.2 \
    numpy==1.24.4 \
    kaleido==0.1.0post1 \
    plotly==5.14.1 \
    NanoPlot==1.42.0

WORKDIR /pipeline
COPY scripts/ ./scripts/
