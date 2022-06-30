from robot.api.logger import error, warn, info, debug, trace, console
import requests

class AppServer:
    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(self) -> None:
        self.session = requests.Session()
        self.app_base = "http://localhost:8082/"

    def is_appserver_up(self) -> bool:
        return self.get_all_appserver_devices() is not None

    def get_all_appserver_devices(self):
        return object()
