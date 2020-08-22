#!/usr/bin/python3
""" deletes old versions"""

from fabric import api
import os


api.env.user = 'ubuntu'
api.env.hosts = ['3.80.226.140', '54.83.103.89']


def do_clean(number=0):
        """ Deletes olds versions """
        if number == 0 or number == 1:
                with cd.local('./versions/'):
                        local("ls -lv | rev | cut -f 1 | rev | \
                        head -n +1 | xargs -d '\n' rm -rf")
                with cd('/data/web_static/releases/'):
                        run("sudo ls -lv | rev | cut -f 1 | \
                        rev | head -n +1 | xargs -d '\n' rm -rf")
        else:
                with cd.local('./versions/'):
                        local("ls -lv | rev | cut -f 1 | rev | \
                        head -n +{} | xargs -d '\n' rm -rf".format(number))
                with cd('/data/web_static/releases/'):
                        run("sudo ls -lv | rev | cut -f 1 | \
                        rev | head -n +{} | xargs -d '\n' rm \
                        -rf".format(number))
