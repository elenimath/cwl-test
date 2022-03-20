FROM python:3.8-slim

# install dependencies
RUN pip install argparse numpy pandas scipy
RUN pip install neo

# copy python script, make executable and add to path
COPY analysis.py /home/tool/analysis.py
RUN chmod +x /home/tool/analysis.py
ENV PATH="/home/tool:$PATH"

CMD [ "/bin/bash" ]
