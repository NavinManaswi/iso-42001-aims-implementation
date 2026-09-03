# AIMS Scope Statement

**Organization:** NovaTech Financial Group  
**Document ID:** AIMS-SCOPE-2026-001  
**Effective Date:** 1 March 2026  
**Version:** 1.0  
**Owner:** Chief AI Officer (CAIO)

---

## 1. Purpose

This document defines the scope of NovaTech's AI Management System (AIMS) in accordance with ISO/IEC 42001:2026, Clause 4.3. It establishes the boundaries of the AIMS, identifying which AI systems, processes, business units, and geographic locations are covered.

---

## 2. Scope Definition

The AIMS applies to all AI systems that:

1. **Process personal data** of EU/UK/US residents
2. **Make autonomous decisions** affecting customer financial well-being
3. **Are classified as High-Risk** under the EU AI Act (Annex III)
4. **Are used in critical business operations** (as defined by NovaTech's Risk Appetite Statement)
5. **Are developed, procured, or operated** by or on behalf of NovaTech

---

## 3. In-Scope AI Systems

| System | Business Unit | Risk Tier | Jurisdiction | AI System Type |
|--------|---------------|-----------|--------------|----------------|
| CreditIQ | Retail Lending | High-Risk | Global | Predictive (XGBoost) |
| InsureScore | Insurance | High-Risk | US, EU | Predictive (Gradient Boosting) |
| RecruitAI | HR | High-Risk | US, EU | Predictive (Ensemble) |
| FraudShield | Payments | High-Risk | Global | Predictive (Random Forest) |
| MarketPredict | Wealth Management | Limited-Risk | Global | Predictive (LSTM) |
| NovaChat | Wealth Management | Limited-Risk | Global | Generative (LLM) |

---

## 4. Out-of-Scope AI Systems

| System | Business Unit | Rationale for Exclusion |
|--------|---------------|--------------------------|
| Internal Meeting Scheduler | IT | Minimal-risk; internal use only; no customer data |
| Spam Filter | IT | Minimal-risk; commodity tool; no regulatory impact |
| Code Completion Tool | Engineering | Minimal-risk; internal development only |
| Employee Wellness Chatbot | HR | Limited-risk; internal use; no sensitive data |

---

## 5. Geographic Scope

| Region | Countries/States |
|--------|------------------|
| North America | United States (all states), Canada |
| European Union | All 27 member states |
| United Kingdom | England, Scotland, Wales, Northern Ireland |
| Asia-Pacific | Australia, Singapore, Japan (limited deployment) |

---

## 6. Organizational Scope

The AIMS applies to:
- All NovaTech subsidiaries
- All joint ventures where NovaTech has operational control
- All third-party vendors providing AI services to NovaTech

The AIMS does not apply to:
- Independent contractors (except where they process data on behalf of NovaTech)
- Acquired companies during their integration period (90 days)

---

## 7. Process Scope

The AIMS covers the full AI lifecycle:

| Phase | Activities |
|-------|------------|
| **Design** | Requirements definition, UCCF classification, data governance |
| **Build** | Model development, secure coding, training, validation |
| **Test** | Performance testing, bias testing, security testing |
| **Deploy** | Deployment approval, human oversight, monitoring setup |
| **Operate** | Continuous monitoring, incident response, post-market monitoring |
| **Retire** | Model retirement, data deletion, archival |

---

## 8. Exclusions

| Exclusion | Rationale |
|-----------|-----------|
| Non-AI automation | Traditional rule-based systems without ML components |
| Legacy systems | Systems in maintenance mode with no active development |
| Preliminary research | Exploratory AI not intended for production |

---

## 9. Scope Review

The AIMS scope shall be reviewed annually by the AI Governance Council and updated as needed.

| Review Date | Status | Next Review |
|-------------|--------|-------------|
| 1 March 2026 | Complete | 1 March 2027 |

---

## 10. Signatories

| Signatory | Title | Signature | Date |
|-----------|-------|-----------|------|
| | Chief AI Officer | | |
| | Chief Risk Officer | | |
| | Board AI Oversight Committee Chair | | |

---

## 11. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 1 March 2026 | CAIO | Initial version |
