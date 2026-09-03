# AI Risk Assessment

**Document ID:** AIMS-RA-2026-001  
**Date:** 15 August 2026  
**Clause:** 6.1.2 — AI Risk Assessment  
**System:** CreditIQ

---

## 1. Risk Identification

| Risk ID | Description | Source | Category |
|---------|-------------|--------|----------|
| R-001 | Algorithmic bias — disparate impact across racial groups | Bias testing | Fairness |
| R-002 | Unexplainable outputs — ECOA compliance risk | Model validation | Transparency |
| R-003 | Economic drift — model instability during recessions | Performance monitoring | Reliability |
| R-004 | Adversarial tampering — fraud vulnerability | Security testing | Security |
| R-005 | Regulatory breach — EU AI Act non-compliance | Gap assessment | Legal/Compliance |
| R-006 | Data privacy breach — unauthorized access to PII | Privacy assessment | Privacy |
| R-007 | Cascading failure — manual fallback overwhelmed | Capacity planning | Resilience |

---

## 2. Risk Analysis

| Risk ID | Likelihood | Impact | Inherent Risk | Controls | Status |
|---------|------------|--------|---------------|----------|--------|
| R-001 | High | Critical | Critical | Pre-processing bias mitigation; quarterly audits | In Progress |
| R-002 | Medium | High | High | LIME explanations; human review | In Progress |
| R-003 | High | High | High | Weekly monitoring; kill-switch | In Progress |
| R-004 | Low | Medium | Medium | Rate limiting; anomaly detection | Planned |
| R-005 | Medium | High | High | Annex IV documentation; mock audits | In Progress |
| R-006 | Medium | High | High | Differential privacy; access controls | In Progress |
| R-007 | Low | High | High | Cross-training; capacity planning | Planned |

---

## 3. Risk Evaluation & Treatment

| Risk ID | Treatment Decision | Treatment Plan | Owner | Target Date | Residual Risk |
|---------|-------------------|----------------|-------|-------------|---------------|
| R-001 | Mitigate | Reweight training samples; hard fairness constraint; quarterly third-party audits | Head of Model Validation | 15 Sep 2026 | Medium |
| R-002 | Mitigate | Implement SHAP explanations; train simpler fallback model | ML Ops | 30 Nov 2026 | Medium |
| R-003 | Mitigate | Weekly PSI monitoring; automatic tempering at 0.2 PSI | ML Ops | 15 Oct 2026 | Medium |
| R-004 | Accept | Rate limiting and encryption implemented | CISO | N/A | Low |
| R-005 | Mitigate | Complete Annex IV docs; mock regulatory inspection | AI Compliance | 15 Oct 2026 | Medium |
| R-006 | Mitigate | Differential privacy; enhanced audit logging | Privacy Officer | 30 Nov 2026 | Low |
| R-007 | Mitigate | Cross-train 50 additional underwriters; stress test | Underwriting Manager | 1 Jan 2027 | Medium |

---

## 4. Risk Acceptance

| Risk ID | Residual Risk | Acceptance Criteria | Approved By | Date |
|---------|---------------|---------------------|-------------|------|
| R-001 | Medium | DIR > 75% with quarterly monitoring | Head of Model Risk | 15 Aug 2026 |
| R-002 | Medium | Underwriter understanding > 90% | CAIO | 15 Aug 2026 |
| R-003 | Medium | Automatic tempering at 0.2 PSI | ML Ops | 15 Aug 2026 |
| R-004 | Low | Security controls in place | CISO | 15 Aug 2026 |
| R-005 | Medium | Docs complete by Q4 2026 | AI Compliance | 15 Aug 2026 |
| R-006 | Low | Privacy controls in place | Privacy Officer | 15 Aug 2026 |
| R-007 | Medium | Capacity tested by Q1 2027 | Underwriting | 15 Aug 2026 |

---

## 5. Overall Risk Assessment

| Metric | Value |
|--------|-------|
| **Total Risks Identified** | 7 |
| **Critical Risks** | 1 |
| **High Risks** | 5 |
| **Medium Risks** | 1 |
| **Residual Risk Rating** | **Medium** |
| **Risk Appetite Alignment** | ✅ Within appetite (with conditions) |

---

## 6. Signatories

| Signatory | Title | Signature | Date |
|-----------|-------|-----------|------|
| | Head of Model Risk | | |
| | CAIO | | |
| | AI Governance Council Chair | | |

---

## 7. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 15 Aug 2026 | Model Risk | Initial version |
