# Okta Federal Zero-Trust Lab
      Okta Federal Zero Trust Identity Lab
Author: Bolaji Ajayi

Tenant: https://trial-6169156.okta.com

Focus: Zero Trust, Modern + Legacy Apps, MFA/FIDO2, Privileged Access, SCIM Lifecycle, AWS OIDC, API Automation


      Project Overview
This project simulates a complete federal-grade Zero Trust identity architecture using the Okta Workforce Identity Cloud. It includes both modern (OIDC) and legacy (SAML) application integrations, phishing-resistant authentication, privileged access controls, lifecycle automation concepts, and multi-cloud identity federation.
This lab aligns directly with federal Zero Trust requirements (NIST 800-207) and with the responsibilities of an Okta Senior Solutions Engineer (Federal).
      
      Key Capabilities Implemented
            OIDC integration (modern case management portal)
            SAML 2.0 integration (legacy HR/payroll system)
            Zero Trust app sign-on policies
            Phishing-resistant MFA (WebAuthn/FIDO2 + Okta Verify)
            Privileged Access (JIT/PAM) with admin FIDO2-only rules
            SCIM lifecycle architecture (conceptual)
            AWS OIDC federation model
            Okta API automation (Python)
            Screenshots & documentation for proof-of-work
            Audit + SIEM logging flow (Splunk / Sentinel)

      Identity Groups Used
            Federal-Users → OIDC + SAML access, MFA required
            Federal-Admins → FIDO2-only privileged access
            PAM-Session-Reviewers → analyzes privileged actions

      Zero Trust Policies
            OIDC App — Case Management Portal
            MFA required (Okta Verify / WebAuthn)
            Block high-risk login attempts (new device, unknown network, outside US)
            SAML App — Legacy HR System
            Admins: FIDO2-only, strict access
            Users: MFA required

      Privileged Access (JIT / PAM Model)
            Admin authenticates via FIDO2
            Okta checks device, risk, and network
            Admin receives temporary elevated privileges
            All privileged activity is logged
            PAM-Session-Reviewers review logs in SIEM
            This simulates federal privileged access governance.

      Documentation
            SCIM Lifecycle Architecture
            → docs/scim-lifecycle.md
            AWS OIDC Integration
            → docs/aws-oidc.md
            API Automation (Python Examples)
            → docs/api-automation.md
            Full Federal POC Document
            → (poc/POC_Document.md) 



      API Scripts
            Example Python user creation script is located at:
            → api/create_user.py
            Demonstrates REST API and automation usage.


      Screenshots
            All screenshots of your Okta setup go here:
            → screenshots/
            
            This includes:
                        App integrations
                        MFA settings
                        Groups
                        Policies
                        User flows
            
                  Diagrams
            Place architectural diagrams in:
            → diagrams/
            
            Planned diagrams:
            
                        Zero Trust Architecture
                        SCIM Lifecycle Flow
                        AWS OIDC Flow
                        JIT/PAM Flow
            

            
                        Summary
            This lab demonstrates how Okta’s Workforce Identity Cloud can secure workforce identities in a federal environment through Zero Trust principles, modern authentication protocols, app modernization, privileged access controls, lifecycle governance, and multi-cloud federation.
