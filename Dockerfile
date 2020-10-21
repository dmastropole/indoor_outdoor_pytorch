FROM pytorch/pytorch:1.6.0-cuda10.1-cudnn7-runtime

# Installs
RUN apt-get update && \
    apt-get install -y wget && \
	apt-get install -y vim && \
	apt-get install -y libffi-dev python-dev build-essential && \
	apt install -y zip

# Expose prts for jupyter notebooks
EXPOSE 8888
EXPOSE 5000

RUN mkdir /home/indoor_outdoor_pytorch
WORKDIR /home/indoor_outdoor_pytorch

# copy current dir
COPY . .

# install the requirements.txt packages
RUN pip install --no-cache-dir -r requirements.txt

# add some jupyter configurations
RUN jupyter notebook --generate-config
RUN echo "c.NotebookApp.ip = '0.0.0.0'" >> ~/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.allow_root = True" >> ~/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.open_browser = False" >> ~/.jupyter/jupyter_notebook_config.py
RUN jupyter nbextension enable --py widgetsnbextension

CMD ["/bin/bash"]
