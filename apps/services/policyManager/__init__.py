
from flask import Blueprint

blueprint = Blueprint(
    'policyManager_blueprint',
    __name__,
    url_prefix='/policyManager'
)
