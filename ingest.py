import yaml
from functions.request_endpoint import request_endpoint
from functions.data_reader import yaml_reader
from config.config import settings

data = yaml_reader(
    'config/config.yml'
)

resp = request_endpoint(
    data=data
)