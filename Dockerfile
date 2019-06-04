ARG CMS_TAG=latest
FROM misli/django-cms-site:$CMS_TAG

LABEL name="Nadační fond Františka Buriana"
LABEL maintainer="Jakub Dorňák <jakub.dornak@misli.cz>"

# install other dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy files
COPY nffb /app/nffb

ENV SITE_MODULE=nffb

# run this command at the end of any dockerfile based on this one
RUN django-cms collectstatic --no-input
