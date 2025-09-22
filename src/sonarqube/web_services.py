class SonarQubeWebServices:
    def __init__(self, client):
        self.client = client

    def list_web_services(self, include_internals=None):
        """
        List web services.
        :param include_internals: Include web services that are implemented for internal use only.
        """
        params = {}
        if include_internals:
            params["include_internals"] = include_internals
        return self.client._get("api/webservices/list", params=params)

    def get_web_service_response_example(self, action, controller):
        """
        Display web service response example.
        :param action: Action of the web service.
        :param controller: Controller of the web service.
        """
        params = {"action": action, "controller": controller}
        return self.client._get("api/webservices/response_example", params=params)
