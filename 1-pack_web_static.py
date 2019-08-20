#!/usr/bin/python3
import datetime
from fabric.api import *


def do_pack():
    """ Function generates a .tgz archive from the
        contents of the 'web_static' folder
    """
    local("mkdir -p versions")
    timeStamp = datetime.datetime.now()
    file_name = "versions/web_static_{}.tgz".format(
        timeStamp.strftime("%Y%m%d%H%M%S"))
    string = "tar -czvf {} web_static".format(file_name)
    results = local(string)
    if results.failed:
        return None
    return results
