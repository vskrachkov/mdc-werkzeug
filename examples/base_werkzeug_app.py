"""
    base_werkzeug_app.py
    ====================

    Example of a simple app written using werkzeug library.
"""
import json

import psycopg2
from werkzeug.exceptions import HTTPException
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Response, Request


class Application:
    def __init__(self, config):
        self.postgres_conn = psycopg2.connect(
            database=config.get('POSTGRES_DATABASE_NAME', 'postgres'),
            user=config.get('POSTGRES_DATABASE_USER', 'postgres'),
            password=config.get('POSTGRES_DATABASE_PASSWORD'),
            host=config.get('POSTGRES_HOST', 'localhost'),
            port=config.get('POSTGRES_PORT', 5432)
        )
        self.url_map = Map([
            Rule('/', endpoint='index'),
            Rule('/<name>', endpoint='hello_page'),
            Rule('/json_data', endpoint='json')
        ])

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, url_params = adapter.match()
            controller = getattr(self, 'controller_'+endpoint)
            return controller(request, **url_params)
        except HTTPException as err:
            return err

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    @staticmethod
    def controller_index(request):
        return Response('<h1>Home page</h1>', mimetype='text/html')

    @staticmethod
    def controller_hello_page(request, name):
        return Response(f'<h2>Hello {name}</h2>', mimetype='text/html')

    @staticmethod
    def controller_json(request):
        json_data = json.dumps({
            'first_name': 'Ben',
            'last_name': 'Larson'
        })
        return Response(json_data, mimetype='application/json')

configuration = {
    'POSTGRES_DATABASE_NAME': 'mdc_database',
    'POSTGRES_DATABASE_USER': 'mdc',
    'POSTGRES_DATABASE_PASSWORD': 'BiGveryStrongPassword',
    'POSTGRES_HOST': 'localhost'
}


def create_app(config_dict):
    an_app = Application(config=config_dict)
    return an_app

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app(config_dict=configuration)
    run_simple(hostname='localhost',
               port=8000,
               application=app,
               use_debugger=True,
               use_reloader=True)
