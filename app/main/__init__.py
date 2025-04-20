from flask import Blueprint

main_bp = Blueprint("main", __name__, url_prefix="/", template_folder="templates")

from . import routes  # noqa: E402
