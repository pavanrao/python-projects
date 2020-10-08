import os
import sys
import flask

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

from pypi_org.infrastructure.view_modifiers import response
import pypi_org.services.package_service as package_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = package_service.get_latest_packages()
    return {'packages': test_packages} 
    # return flask.render_template('home/index.html', packages=test_packages)


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {}
    # return flask.render_template('home/about.html')
