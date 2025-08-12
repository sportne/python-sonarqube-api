class SonarQubeEditions:
    def __init__(self, client):
        self.client = client

    def activate_grace_period(self):
        """
        Enable a license 7-days grace period if the Server ID is invalid.
        """
        return self.client._post("api/editions/activate_grace_period")

    def is_valid_license(self):
        """
        Return the validity of the license.
        """
        return self.client._get("api/editions/is_valid_license")

    def set_license(self, license):
        """
        Set the license for enabling features of commercial editions.
        :param license: License key
        """
        params = {"license": license}
        return self.client._post("api/editions/set_license", params=params)

    def show_license(self):
        """
        Show information about currently installed license.
        """
        return self.client._get("api/editions/show_license")

    def unset_license(self):
        """
        Un-sets license.
        """
        return self.client._post("api/editions/unset_license")
