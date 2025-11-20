# Okta Federal Zero-Trust Lab
A full Zero Trust identity architecture using Okta Workforce Identity Cloud (SAML, OIDC, JIT/PAM, SCIM, AWS OIDC, API automation).

Okta Federal Zero Trust Identity Lab
Author: Bolaji Ajayi
Platform: Okta Workforce Identity Cloud
Tenant: https://trial-6169156.okta.com
Focus: Zero Trust, SAML/OIDC, PAM/JIT, SCIM Lifecycle, MFA/FIDO2, Federal IAM


      Overview
This project simulates a federal-grade Zero Trust identity architecture using the Okta Workforce Identity Cloud. The lab covers modern and legacy application integration, phishing-resistant authentication, privileged access modeling, and lifecycle automation. The design aligns with NIST 800-207 and federal identity modernization strategies.

      Key Features
   SAML and OIDC application integrations
   Zero Trust app sign-on policies
   Phishing-resistant MFA (FIDO2/WebAuthn)
   Privileged Access + JIT elevation model
   SCIM lifecycle architecture
   AWS OIDC trust model
   Okta API automation examples
   SIEM logging flow for federal audit readiness

      Identity Groups & Roles
   Federal-Users – Standard workforce access
   Federal-Admins – Privileged identities; FIDO2-only authentication
   PAM-Session-Reviewers – Security team reviewing admin actions


      Applications
OIDC App: Federal Case Management Portal
   OAuth 2.0 / OIDC integration
   Used for modern app federation
SAML App: Legacy HR & Payroll System
   SAML 2.0
   Simulates legacy federal apps used in modernization projects

      Zero Trust Policies
OIDC Zero Trust
   Rule 1: Require MFA (Federal-Users)
   Rule 2: Deny high-risk login attempts
SAML Zero Trust
   Admin Only Rule → FIDO2 Only
   User Rule → MFA required, limited privileges

      Privileged Access (JIT/PAM Model)
Workflow:
   Admin authenticates with FIDO2
   Okta verifies device, risk, IP
   Temporary admin access is granted
   Privileged actions logged to SIEM
   PAM-Session-Reviewers analyze logs
This demonstrates a federal-grade privileged access model.

Additional Documentation
      SCIM Lifecycle Architecture
      AWS OIDC Integration
      API Automation Examples

      Logging & SIEM
Events streamed to Splunk/Sentinel:
      MFA attempts
      WebAuthn authentication
      App sign-on allow/deny
      Admin elevation
      Group changes
      Anomaly detection
      Supports federal audit & compliance.

   
      Competitive Positioning
      
   Okta vs Azure AD
   Okta = neutral, multi-cloud
   Azure AD = tied to Microsoft ecosystem
   Okta = stronger app integrations
   Azure = good for M365 only
   Okta vs Ping
   Okta = cloud-first, faster to deploy
   Ping = enterprise legacy-heavy

      Summary
This lab demonstrates a complete Zero Trust identity architecture for federal environments using Okta Workforce Identity Cloud. It includes:
Modern OIDC
Legacy SAML
MFA/FIDO2
JIT/PAM privileged access
SCIM lifecycle
Multi-cloud OIDC
API automation
Federal audit logging
