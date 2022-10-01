FROM continuumio/miniconda3:4.10.3p1

WORKDIR /project

RUN conda install \
    xarray \ 
    netCDF4 \ 
    bottleneck \
    numpy \
    pandas \
    matplotlib \
    jupyterlab

COPY ./README.md /project
COPY ./data /project/data
COPY ./origin_data /project/origin_data
COPY ./src /project/src
COPY ./notebooks /project/notebooks

CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root"]


