class SonarQubeScaV2:
    def __init__(self, client):
        self.client = client

    def get_risk_reports(self, component, branch=None, riskType=None):
        """
        Get a report for all the current SCA dependency risks for a given component and branch.
        :param component: Key of the component (project, application, portfolio) to build report for.
        :param branch: Key of the branch to build report for.
        :param riskType: Type of risk to filter the report by.
        """
        params = {"component": component}
        if branch:
            params["branch"] = branch
        if riskType:
            params["riskType"] = riskType
        return self.client._get("api/v2/sca/risk-reports", params=params)

    def get_sbom_reports(self, component, type, branch=None):
        """
        Get a software bill of materials (SBOM) report.
        :param component: Key of the component (project, application, portfolio) to build report for.
        :param type: Type of report to generate.
        :param branch: Key of the branch to build report for.
        """
        params = {"component": component, "type": type}
        if branch:
            params["branch"] = branch
        return self.client._get("api/v2/sca/sbom-reports", params=params)
