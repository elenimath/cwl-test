FROM python:3

# install dependencies
RUN pip install argparse numpy pandas matplotlib

# copy python script, make executable and add to path
COPY visualization.py /home/tool/visualization.py
RUN chmod +x /home/tool/visualization.py
ENV PATH="/home/tool:$PATH"

CMD [ "/bin/bash" ]
