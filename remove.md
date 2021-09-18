#COPY ./compose/local/django/celery/beat/start /start-celerybeat
#RUN sed -i 's/\r$//g' /start-celerybeat
#RUN chmod +x /start-celerybeat
