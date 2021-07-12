FROM continuumio/miniconda3
ENV PIP_NO_CACHE_DIR=1 
RUN conda install -f mkl mkl-service
RUN conda install numpy mkl mkl-service
RUN pip install --no-cache-dir fastapi uvicorn
RUN conda install mamba -n base -c conda-forge && conda clean -ay
RUN pip install transformers
RUN pip list
# COPY requirements.txt /requirements.txt
# RUN pip install -r requirements.txt
RUN mkdir -p /webapp
WORKDIR /webapp
COPY . /webapp
EXPOSE 80
ENTRYPOINT ["uvicorn","--host","0.0.0.0","--port","80","routes:app"]