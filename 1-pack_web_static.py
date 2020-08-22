#!/usr/bin/env python3
# compress  the contents of the web_static folder

from fabric.api import run, local, sudo
from datetime import datetime
from os.path import isdir


def do_pack():
    """
    Generate file
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
