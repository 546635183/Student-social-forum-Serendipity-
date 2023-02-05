from flask import Blueprint

# /author
bp = Blueprint("author", __name__, url_prefix="/author")

@bp.route("/login")
def login():
    pass