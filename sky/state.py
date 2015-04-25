import os
import sys
import logging
from .utils import parse_arguments

class Ready(dict):

    def __init__(self):
        super(Ready, self).__init__()

    def __getattr__(self, attr):
        return self[attr]

ready = Ready()

CREATION_MODE = None
EPHEMERAL = 'ephemeral'
PERMANENT = 'permanent'

logger = logging.getLogger(__name__)

args = parse_arguments()
PROJECT_NAME = os.path.abspath(os.path.expanduser(args.directory)).split(os.sep)[-1].lower()
PROJECT_DIRECTORY = os.path.abspath(os.path.expanduser(args.directory)).lower()
ENVIRONMENT = args.environment.lower()
AWS_ACCESS_KEY_ID = args.key_id
AWS_SECRET_ACCESS_KEY = args.key