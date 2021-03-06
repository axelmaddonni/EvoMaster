import abc
import threading
from importlib import import_module
from werkzeug.serving import make_server

from evomaster_client.controller.sut_handler import SutHandler
from evomaster_client.instrumentation.import_hook import install_import_hook

HOST = '127.0.0.1'
PORT = 5000


class ServerThread(threading.Thread):
    def __init__(self, app):
        threading.Thread.__init__(self)
        self.app = app

    def run(self):
        self.srv = make_server(host=HOST, port=PORT, app=self.app)
        self.ctx = self.app.app_context()
        self.ctx.push()
        self.srv.serve_forever()

    def shutdown(self):
        self.srv.shutdown()


class FlaskHandlerError(Exception):
    pass


class FlaskHandler(SutHandler, metaclass=abc.ABCMeta):
    def __init__(self, instrumentation_level: int = None):
        self.server = None  # SUT is not running
        self.instrumentation_level = instrumentation_level

    def app(self):
        print('Importing Flask application')
        module = import_module(self.flask_module())
        app = module.__getattribute__(self.flask_app())
        return app

    def instrumented_app(self):
        with install_import_hook(self.package_prefixes_to_cover(), self.instrumentation_level):
            return self.app()

    @abc.abstractmethod
    def package_prefixes_to_cover(self):
        pass

    @abc.abstractmethod
    def flask_module(self):
        pass

    @abc.abstractmethod
    def flask_app(self):
        pass

    @abc.abstractmethod
    def get_url(self):
        return f'http://{HOST}:{PORT}'

    def start_sut(self):
        if self.is_sut_running():
            print('server is running')
            return
        self.server = ServerThread(self.instrumented_app())
        self.server.start()

    def stop_sut(self):
        if not self.is_sut_running():
            print('server is not running')
            return
        # Server will stop after the next request. TODO: is there a way to force it?
        self.server.shutdown()
        self.server = None

    @abc.abstractmethod
    def reset_state_of_sut(self):
        pass

    @abc.abstractmethod
    def setup_for_generated_test(self):
        pass

    @abc.abstractmethod
    def get_info_for_authentication(self):
        # TODO: must be an argument
        return []

    @abc.abstractmethod
    def get_preferred_output_format(self):
        # TODO: must be an argument
        return 'JAVA_JUNIT_5'

    def is_sut_running(self):
        return bool(self.server)

    @abc.abstractmethod
    def get_problem_info(self):
        # TODO: must be an argument
        return {
            'swaggerJsonUrl': self.get_url() + '/swagger.json',
            'endpointsToSkip': []
        }
