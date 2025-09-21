[Back to Index](index.md)

# Users

### `POST api/users/change_password`
*since 5.2*

Update a user's password. Authenticated users can change their own password, provided that the account is not linked to an external authentication system. Administer System permission is required to change another user's password.

**Parameters**
- `login` (required): User login. Example value: `myuser`
- `password` (required): The password needs to fulfill the following requirements: at least 12 characters and contain at least one uppercase character, one lowercase character, one digit and one special character. Example value: `My_Passw0rd%`. Minimum length: 12
- `previousPassword` (optional): Previous password. Required when changing one's own password. Example value: `My_Previous_Passw0rd%`

---

### `GET api/users/current`
*internal since 5.2*

Get the details of the current authenticated user.

---

### `POST api/users/dismiss_notice`
*internal since 9.6*

Dismiss a notice for the current user. Silently ignore if the notice is already dismissed.

**Parameters**
- `notice` (optional): notice key to dismiss. Possible values: `issueNewIssueStatusAndTransitionGuide`, `overviewZeroNewIssuesSimplification`, `showEnableSca`, `qualityGateCaYCConditionsSimplification`, `educationPrinciples`, `sonarlintAd`, `showNewModesTour`, `showDesignAndArchitectureBanner`, `showNewModesBanner`, `issueCleanCodeGuide`, `onboardingDismissCaycBranchSummaryGuide`, `showDesignAndArchitectureOptInBanner`, `showDesignAndArchitectureTour`. Example value: `EDUCATION_PRINCIPLES`

---

### `GET api/users/identity_providers`
*internal since 5.5*

List the external identity providers

---

### `POST api/users/set_ai_tool_usage`
*internal since 2025.1*

Indicates whether the current user utilizes any tool that generates AI code for a given project.
Requires 'Browse' permission on the specified project.

**Parameters**
- `project` (required): Project key. Example value: `my_project`

---

### `POST api/users/set_homepage`
*internal since 7.0*

Set homepage of current user.
Requires authentication.

**Parameters**
- `branch` (optional): since 7.1, Branch key. It can only be used when parameter 'type' is set to 'PROJECT'. Example value: `feature/my_branch`
- `component` (optional): since 7.1, Project key. It should only be used when parameter 'type' is set to 'PROJECT'. Example value: `my_project`
- `type` (required): Type of the requested page. Possible values: `PROJECT`, `PROJECTS`, `ISSUES`, `PORTFOLIOS`, `PORTFOLIO`, `APPLICATION`
