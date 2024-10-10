
from flask import Blueprint

blueprint = Blueprint(
    's3Manager_blueprint',
    __name__,
    url_prefix='/s3Manager'
)
