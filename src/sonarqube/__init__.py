from .alm_integrations import SonarQubeAlmIntegrations as SonarQubeAlmIntegrations
from .alm_settings import SonarQubeAlmSettings as SonarQubeAlmSettings
from .analysis_cache import SonarQubeAnalysisCache as SonarQubeAnalysisCache
from .analysis_v2 import SonarQubeAnalysisV2 as SonarQubeAnalysisV2
from .applications import SonarQubeApplications as SonarQubeApplications
from .audit_logs import SonarQubeAuditLogs as SonarQubeAuditLogs
from .authentication import SonarQubeAuthentication as SonarQubeAuthentication
from .authorizations_v2 import SonarQubeAuthorizationsV2 as SonarQubeAuthorizationsV2
from .ce import SonarQubeCe as SonarQubeCe
from .clean_code_policy_v2 import (
    SonarQubeCleanCodePolicyV2 as SonarQubeCleanCodePolicyV2,
)
from .client import SonarQubeClient as SonarQubeClient
from .components import SonarQubeComponents as SonarQubeComponents
from .dop_translation_v2 import SonarQubeDopTranslationV2 as SonarQubeDopTranslationV2
from .duplications import SonarQubeDuplications as SonarQubeDuplications
from .editions import SonarQubeEditions as SonarQubeEditions
from .favorites import SonarQubeFavorites as SonarQubeFavorites
from .fix_suggestions_v2 import SonarQubeFixSuggestionsV2 as SonarQubeFixSuggestionsV2
from .hotspots import SonarQubeHotspots as SonarQubeHotspots
from .issues import SonarQubeIssues as SonarQubeIssues
from .languages import SonarQubeLanguages as SonarQubeLanguages
from .measures import SonarQubeMeasures as SonarQubeMeasures
from .metrics import SonarQubeMetrics as SonarQubeMetrics
from .monitoring import SonarQubeMonitoring as SonarQubeMonitoring
from .new_code_periods import SonarQubeNewCodePeriods as SonarQubeNewCodePeriods
from .notifications import SonarQubeNotifications as SonarQubeNotifications
from .permissions import SonarQubePermissions as SonarQubePermissions
from .plugins import SonarQubePlugins as SonarQubePlugins
from .project_analyses import SonarQubeProjectAnalyses as SonarQubeProjectAnalyses
from .project_badges import SonarQubeProjectBadges as SonarQubeProjectBadges
from .project_branches import SonarQubeProjectBranches as SonarQubeProjectBranches
from .project_dump import SonarQubeProjectDump as SonarQubeProjectDump
from .project_links import SonarQubeProjectLinks as SonarQubeProjectLinks
from .project_pull_requests import (
    SonarQubeProjectPullRequests as SonarQubeProjectPullRequests,
)
from .project_tags import SonarQubeProjectTags as SonarQubeProjectTags
from .projects import SonarQubeProjects as SonarQubeProjects
from .quality_gates import SonarQubeQualityGates as SonarQubeQualityGates
from .quality_profiles import SonarQubeQualityProfiles as SonarQubeQualityProfiles
from .rules import SonarQubeRules as SonarQubeRules
from .sca_v2 import SonarQubeScaV2 as SonarQubeScaV2
from .server import SonarQubeServer as SonarQubeServer
from .settings import SonarQubeSettings as SonarQubeSettings
from .sources import SonarQubeSources as SonarQubeSources
from .system import SonarQubeSystem as SonarQubeSystem
from .system_v2 import SonarQubeSystemV2 as SonarQubeSystemV2
from .user_tokens import SonarQubeUserTokens as SonarQubeUserTokens
from .users import SonarQubeUsers as SonarQubeUsers
from .users_v2 import SonarQubeUsersV2 as SonarQubeUsersV2
from .views import SonarQubeViews as SonarQubeViews
from .web_services import SonarQubeWebServices as SonarQubeWebServices
from .webhooks import SonarQubeWebhooks as SonarQubeWebhooks

SonarQube = SonarQubeClient
