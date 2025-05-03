from os import sep
from os.path import dirname
from sys import path

path.append(sep.join([dirname(dirname(__file__)), "main"]))
