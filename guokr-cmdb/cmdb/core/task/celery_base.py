# -*- coding: utf-8 -*-
from flask import has_app_context
from celery import Celery

def make_celery():
    from cmdb import create_app
    capp = create_app()
    celery = Celery(__name__, broker=capp.config['CELERY_BROKER_URL'])
    celery.conf.update(capp.config)
    TaskBase = celery.Task
    celery.flask = capp
    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            if has_app_context():
                return TaskBase.__call__(self, *args, **kwargs)
            else:
                with capp.app_context():
                    return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery
celery = make_celery()
