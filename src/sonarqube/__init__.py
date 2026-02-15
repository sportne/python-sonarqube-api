from .analysis_v2 import SonarQubeAnalysisV2 as SonarQubeAnalysisV2
from .authorizations_v2 import SonarQubeAuthorizationsV2 as SonarQubeAuthorizationsV2
from .clean_code_policy_v2 import (
    SonarQubeCleanCodePolicyV2 as SonarQubeCleanCodePolicyV2,
)
from .client import SonarQubeClient as SonarQubeClient
from .dop_translation_v2 import SonarQubeDopTranslationV2 as SonarQubeDopTranslationV2
from .fix_suggestions_v2 import SonarQubeFixSuggestionsV2 as SonarQubeFixSuggestionsV2
from .sca_v2 import SonarQubeScaV2 as SonarQubeScaV2
from .sources import SonarQubeSources as SonarQubeSources
from .system_v2 import SonarQubeSystemV2 as SonarQubeSystemV2
from .users_v2 import SonarQubeUsersV2 as SonarQubeUsersV2
from .views import SonarQubeViews as SonarQubeViews
from .web_services import SonarQubeWebServices as SonarQubeWebServices
from .webhooks import SonarQubeWebhooks as SonarQubeWebhooks

SonarQube = SonarQubeClient
