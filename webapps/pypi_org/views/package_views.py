import os
import sys
import flask

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

from pypi_org.infrastructure.view_modifiers import response
import pypi_org.services.package_service as package_service

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
#@response(template_file='packages/details.html')
def package_details(package_name: str):
    return f"Package details for {package_name}"


@blueprint.route('/<int:rank>')
#@response(template_file='packages/details.html')
def popular(rank: int):
    return f"Package details for {rank}th most popular package"
