#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """compress a file"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive = "web_static_{}".format(date)
    path = "versions/{}.tgz web_static".format(archive)
    try:
        local("sudo mkdir -p versions")
        local("tar -cvzf " + path)
        return "versions/{}.tgz".format(archive)
    except:
        return None
