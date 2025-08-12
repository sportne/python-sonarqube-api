import requests

from .applications import SonarQubeApplications
from .ce import SonarQubeCe
from .components import SonarQubeComponents
from .duplications import SonarQubeDuplications
from .editions import SonarQubeEditions
from .favorites import SonarQubeFavorites
from .hotspots import SonarQubeHotspots
from .issues import SonarQubeIssues
from .languages import SonarQubeLanguages
from .measures import SonarQubeMeasures
from .metrics import SonarQubeMetrics
from .monitoring import SonarQubeMonitoring
from .new_code_periods import SonarQubeNewCodePeriods
from .notifications import SonarQubeNotifications
from .permissions import SonarQubePermissions
from .plugins import SonarQubePlugins
from .project_analyses import SonarQubeProjectAnalyses
from .project_badges import SonarQubeProjectBadges
from .project_branches import SonarQubeProjectBranches
from .project_dump import SonarQubeProjectDump
from .project_links import SonarQubeProjectLinks
from .project_pull_requests import SonarQubeProjectPullRequests
from .project_tags import SonarQubeProjectTags
from .projects import SonarQubeProjects
from .quality_gates import SonarQubeQualityGates
from .quality_profiles import SonarQubeQualityProfiles
from .rules import SonarQubeRules
from .system import SonarQubeSystem
from .users import SonarQubeUsers


class SonarQubeClient:
    def __init__(self, host=None, token=None, user=None, password=None):
        """
        Create a SonarQube API client.
        :param host: SonarQube host, eg. http://localhost:9000
        :param token: SonarQube user token
        :param user: SonarQube user
        :param password: SonarQube password
        """
        self.host = host
        self.token = token
        self.user = user
        self.password = password

        # Configure authentication
        self.session = requests.Session()
        if self.token:
            self.session.auth = (self.token, "")
        elif self.user and self.password:
            self.session.auth = (self.user, self.password)

        # Attach API endpoints
        self.applications = SonarQubeApplications(self)
        self.ce = SonarQubeCe(self)
        self.components = SonarQubeComponents(self)
        self.duplications = SonarQubeDuplications(self)
        self.editions = SonarQubeEditions(self)
        self.favorites = SonarQubeFavorites(self)
        self.hotspots = SonarQubeHotspots(self)
        self.issues = SonarQubeIssues(self)
        self.languages = SonarQubeLanguages(self)
        self.measures = SonarQubeMeasures(self)
        self.metrics = SonarQubeMetrics(self)
        self.monitoring = SonarQubeMonitoring(self)
        self.new_code_periods = SonarQubeNewCodePeriods(self)
        self.notifications = SonarQubeNotifications(self)
        self.permissions = SonarQubePermissions(self)
        self.plugins = SonarQubePlugins(self)
        self.project_analyses = SonarQubeProjectAnalyses(self)
        self.project_badges = SonarQubeProjectBadges(self)
        self.project_branches = SonarQubeProjectBranches(self)
        self.project_dump = SonarQubeProjectDump(self)
        self.project_links = SonarQubeProjectLinks(self)
        self.project_pull_requests = SonarQubeProjectPullRequests(self)
        self.project_tags = SonarQubeProjectTags(self)
        self.projects = SonarQubeProjects(self)
        self.quality_gates = SonarQubeQualityGates(self)
        self.quality_profiles = SonarQubeQualityProfiles(self)
        self.rules = SonarQubeRules(self)
        self.system = SonarQubeSystem(self)
        self.users = SonarQubeUsers(self)

    def _get(self, endpoint, **kwargs):
        """
        Send a GET request to the SonarQube API.
        """
        return self.session.get(f"{self.host}/{endpoint}", **kwargs)

    def _post(self, endpoint, **kwargs):
        """
        Send a POST request to the SonarQube API.
        """
        return self.session.post(f"{self.host}/{endpoint}", **kwargs)

    def is_authenticated(self):
        """
        Check if the client is authenticated.
        """
        response = self._get("api/authentication/validate")
        return response.status_code == 200 and response.json().get("valid") is True
