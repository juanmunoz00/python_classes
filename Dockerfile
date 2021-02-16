FROM python:3

RUN apt-get update && apt-get install -y --no-install-recommends \     
	unixodbc-dev \     
	unixodbc \     
	libpq-dev

RUN pip install matplotlib
RUN pip install pandas
RUN pip install scipy
RUN pip install numpy
RUN pip install seaborn
RUN pip install pyodbc
RUN pip install sklearn
RUN pip install xlwt 
RUN pip install xlrd
RUN pip install alive_progress
RUN pip install progressbar
RUN pip install openpyxl

VOLUME /scripts
WORKDIR /scripts

ENTRYPOINT ["python"]
