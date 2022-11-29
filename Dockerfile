FROM python:3.10

ENV MY_PATH=""

ADD main.py requirements.txt file_analyzer.py /
ADD helper.py /
ADD data/* /data/
RUN mkdir results

RUN pip install -r requirements.txt

#CMD python main.py --path $MY_PATH

ENTRYPOINT ["python", "main.py"]