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

---

### `POST api/users/create`
*since 2.0*

Create a user. If a deactivated user account exists with the given login, it will be reactivated.
Requires Administer System permission.

**Parameters**
- `login` (required): User login. Min length 2, max length 255. Example value: `myuser`
- `name` (required): User name. Max length 200. Example value: `My Name`
- `password` (optional): User password. Only mandatory when creating local user, otherwise it should not be set.
- `email` (optional): User email. Example value: `myname@email.com`
- `scmAccounts` (optional): Comma-separated list of SCM accounts.
- `local` (optional): Specify if the user should be authenticated from SonarQube server or from an external authentication system. Default value: `true`.

---

### `POST api/users/deactivate`
*since 3.7*

Deactivate a user. Requires Administer System permission.

**Parameters**
- `login` (required): User login. Example value: `myuser`
- `anonymize` (optional): Anonymize user in addition to deactivating it. Example value: `true`

---

### `GET api/users/groups`
*since 5.2*

Lists the groups a user belongs to. Requires Administer System permission.

**Parameters**
- `login` (required): User login. Example value: `admin`
- `q` (optional): Limit search to group names that contain the supplied string. Example value: `users`
- `selected` (optional): Depending on the value, show only selected items (selected=selected), deselected items (selected=deselected), or all of them (selected=all). Possible values: `all`, `deselected`, `selected`. Default value: `selected`

---

### `GET api/users/search`
*since 3.6*

Get a list of active users.

**Parameters**
- `q` (optional): Filter on login, name and email. Example value: `admin`
- `deactivated` (optional): Return deactivated users instead of active users. Default value: `false`
- `managed` (optional): Return managed or non-managed users. Only available for managed instances. Default value not set.
- `lastConnectedAfter` (optional): Filter the users based on the last connection date field. Only users who interacted with this instance at or after the date will be returned. Format: yyyy-MM-dd
- `lastConnectedBefore` (optional): Filter the users based on the last connection date field. Only users that never connected or who interacted with this instance at or before the date will be returned. Format: yyyy-MM-dd
- `sonarLintLastConnectionDateFrom` (optional): Filter users by SonarLint last connection date (>= this date)
- `sonarLintLastConnectionDateTo` (optional): Filter users by SonarLint last connection date (<= this date)

---

### `POST api/users/update`
*since 3.7*

Update a user. Requires Administer System permission.

**Parameters**
- `login` (required): User login. Example value: `myuser`
- `name` (optional): User name. Example value: `My New Name`
- `email` (optional): User email. Example value: `myname@email.com`
- `scmAccounts` (optional): Comma-separated list of SCM accounts.
