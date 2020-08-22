#!/usr/bin/python3
""" Fabric script deploy all the app """

from fabric.api import *
from os import path
from os.path import isdir


env.hosts = ['3.80.226.140', '54.83.103.89']


def do_pack():
    """
    Generate file.tgz
    """
    try:
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        if isdir("versions") is False:
            local("mkdir versions")
        f = 'versions/web_static_' + time + '.tgz'
        local('tar -cvzf {} web_static'.format(f))
        return f
    except:
        return None


def do_deploy(archive_path):
    """ Distributes an archive to a web server """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """ deploy all  """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
