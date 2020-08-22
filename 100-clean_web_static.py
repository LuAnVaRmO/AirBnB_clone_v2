#!/usr/bin/python3
""" deletes old versions"""

from fabric import api
import os


api.env.user = 'ubuntu'
api.env.hosts = ['3.80.226.140', '54.83.103.89']


def do_clean(number=0):
        """ Deletes olds versions """
        n = int(number)
        if n == 0:
                n = 1
        versions = sorted(os.listdir("versions"))
        for files in range(number):
                versions.pop()
        with api.lcd("versions"):
                for fl in versions:
                        api.local("rm {}".format(fl))

        with cd("/data/web_static/releases/"):
                vers_files = api.run("ls -tr").split()
        fls = []
        for f in vers_files:
                if "web_static" in f:
                        fls.append(f)
                for f in range(n):
                        vers_files.pop()
                for f in vers_files:
                        api.run("rm -rf ./{}".format(f))
