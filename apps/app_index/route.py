from flask import Blueprint
from dao.mysql_operation import IndexOperation

bl_index = Blueprint('index', __name__, url_prefix="/index")


@bl_index.route("/encourage", methods=['GET'])
def encourage():
    res = IndexOperation().encourage()
    return str(res)
