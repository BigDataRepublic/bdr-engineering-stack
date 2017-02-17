FROM continuumio/miniconda3:latest

#RUN apt-get  -y update; yum clean all
#RUN yum -y install epel-release; yum clean all
#RUN yum -y install python-pip; yum clean all
RUN apt-get install -y git python-pip

ADD . /ds_prod


RUN conda env create -f /ds_prod/environment.yml -n "ds_prod"
RUN bash -c "source activate ds_prod"

RUN pip install git+https://github.com/BigDataRepublic/bdr-engineering-stack.git@Feature/model_docker#egg=ds_prod_api&subdirectory=data-science-production-container/ds_prod_api

#CMD ["python", "/ds_prod/SanderTest.py"]
