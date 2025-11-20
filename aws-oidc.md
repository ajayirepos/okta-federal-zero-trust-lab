    AWS OIDC Integration Model
This document explains how Okta federates identities into AWS workloads using OAuth/OIDC tokens.

    Architecture Overview
Okta (OIDC IdP)
     │ issues ID Token
     ▼
AWS Cognito / ALB
     │ validates token
     ▼
AWS Application

    Key Points
    Okta enforces Zero Trust (MFA, risk, device) before AWS grants access
    AWS trusts Okta’s tokens, not passwords
    Works across AWS GovCloud or standard commercial regions
You use this model in federal multi-cloud identity modernization projects.
