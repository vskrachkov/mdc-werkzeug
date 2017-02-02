"""
    base_wsgi_app.py
    ================

    Example of a basic wsgi app using werkzeug Response and Request objects.
"""

from werkzeug.wrappers import Response, Request


def app(environ, start_response):
    """It's a basic wsgi app.
    Args::
        :environ: environ dict contains all incoming information.
        :start_response: a callable can be used to indicate
            the start of response.

        Request takes environ object and allows access the data from that
    environ.
    """
    request = Request(environ)
    text = request.args.get('argument')
    response = Response(mimetype='text/plain')
    return response(environ, start_response)
