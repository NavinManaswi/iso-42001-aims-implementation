# Roles & Responsibilities for AI Management

**Document ID:** AIMS-RACI-2026-001  
**Effective Date:** 1 March 2026  
**Clause:** 5.3 — Organizational Roles, Responsibilities, and Authorities

---

## 1. Purpose

This document defines the roles, responsibilities, and authorities for NovaTech's AI Management System in accordance with ISO/IEC 42001:2026, Clause 5.3.

---

## 2. RACI Definitions

| Code | Meaning | Description |
|------|---------|-------------|
| **R** | Responsible | Performs the work to complete the task |
| **A** | Accountable | Ultimately answerable for the task outcome (only one "A" per task) |
| **C** | Consulted | Input is required before the task is completed |
| **I** | Informed | Must be kept up-to-date on task progress |

---

## 3. Key Roles

### 3.1 Chief AI Officer (CAIO)

| Responsibility | Authority |
|----------------|-----------|
| Own the AIMS and report to Board AI Oversight Committee | Approve AI policies and standards |
| Chair the AI Governance Council | Escalate to Board |
| Allocate AIMS resources | Approve AIMS budget |
| Ensure compliance with ISO 42001 | Certify AIMS readiness |

### 3.2 AI Governance Council

| Responsibility | Authority |
|----------------|-----------|
| Approve AI risk classification | Classify high-risk systems |
| Oversee AI incidents | Escalate to Board |
| Review AI performance | Approve policy changes |

### 3.3 Head of Model Risk

| Responsibility | Authority |
|----------------|-----------|
| Conduct AI Risk Assessments | Approve model validation |
| Test for bias and fairness | Block non-compliant models |
| Monitor model performance | Alert on model drift |

### 3.4 System Owner

| Responsibility | Authority |
|----------------|-----------|
| Ensure AI system compliance | Accept residual risk |
| Maintain documentation | Escalate incidents |
| Implement controls | Approve deployments |

### 3.5 AI Compliance Officer

| Responsibility | Authority |
|----------------|-----------|
| Maintain EU AI Act documentation | Approve regulatory filings |
| Track regulatory changes | Escalate compliance gaps |
| Manage audit evidence | Certify compliance readiness |

---

## 4. RACI Matrix

| Activity | CAIO | AI Council | Model Risk | System Owner | Compliance | Legal | CISO | HR |
|----------|------|------------|------------|--------------|------------|-------|------|-----|
| **Policy & Governance** |
| Draft AI Policy | R | C | C | C | A | C | C | I |
| Approve AI Policy | C | A | C | C | C | C | C | I |
| Define Risk Appetite | C | A | C | C | C | C | I | I |
| **Risk Management** |
| Classify AI System | I | A | R | C | C | C | C | I |
| Conduct AI Risk Assessment | I | C | A | R | C | C | C | I |
| Approve Risk Acceptance | I | A | C | R | C | C | I | I |
| **Compliance** |
| Maintain EU AI Act Docs | C | C | C | R | A | C | I | I |
| File Regulatory Notifications | I | I | I | C | R | A | I | I |
| Respond to Regulatory Inquiry | C | C | C | C | R | A | I | I |
| **Monitoring & Incident** |
| Monitor AI Performance | I | I | A | R | C | I | C | I |
| Detect AI Incident | I | I | I | R | C | I | A | I |
| Respond to AI Incident | C | C | C | R | C | C | A | I |
| **Audit** |
| Prepare Audit Evidence | I | I | C | R | A | C | C | I |
| Internal Audit | I | I | C | C | C | C | C | I |
| External Audit | I | I | C | R | A | C | C | I |

---

## 5. Role Accountability Framework

| Role | Primary Accountability |
|------|------------------------|
| **CAIO** | Overall AIMS effectiveness |
| **AI Governance Council** | AI risk classification and oversight |
| **Head of Model Risk** | AI risk assessment quality |
| **System Owner** | System-level compliance |
| **AI Compliance Officer** | Regulatory compliance |
| **CISO** | AI security and incident response |
| **HR** | AI literacy training and culture |

---

## 6. Escalation Paths

| Scenario | Escalation Path |
|----------|-----------------|
| **Classification dispute** | AI Risk WG → AI Governance Council |
| **Material risk finding** | Model Risk → CAIO → AI Governance Council |
| **Major incident** | CISO → CAIO → AI Governance Council → Board |
| **Regulatory inquiry** | Legal → CAIO → AI Governance Council |
| **Audit finding** | Internal Audit → CAIO → Board Audit Committee |

---

## 7. Review Cycle

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Role review | Annual | CAIO |
| RACI matrix update | Annual | CAIO |
| Competence assessment | Annual | HR + CAIO |
