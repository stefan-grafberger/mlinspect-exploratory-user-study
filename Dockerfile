FROM python:3.9

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y python3-dev graphviz libgraphviz-dev pkg-config

RUN git clone https://github.com/stefan-grafberger/mlinspect-exploratory-user-study.git
WORKDIR "/mlinspect-exploratory-user-study"

RUN pip install --upgrade  --no-binary numpy==1.19.5 numpy==1.19.5 && pip install -e .

CMD ["jupyter", "notebook", "--port", "8899", "--allow-root", "--ip", "0.0.0.0"]
