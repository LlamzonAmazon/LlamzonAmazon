<p align="center">
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg"><img src="assets/header-light.svg" alt="Terminal card: thomas@llamzon, Forward Deployed Engineer, security and full-stack, BSc Honours CS at Western University, first-author IEEE GLOBECOM 2026" width="100%"></picture>
</p>

<p>
  <a href="https://llamzon.ca"><img src="assets/badges/website.svg" alt="Website"></a>
  <a href="https://www.linkedin.com/in/thomasllamzon"><img src="assets/badges/linkedin.svg" alt="LinkedIn"></a>
  <a href="https://github.com/LlamzonAmazon/asynchronous-fl/blob/main/paper/main-conference.pdf"><img src="assets/badges/paper.svg" alt="IEEE GLOBECOM 2026 paper"></a>
</p>

Production AI agents for food and beverage operators, built with a SOC analyst's habits: access control, audit trails and data boundaries from day one.

## Now

**Trellum**: agent platform for an F&B operator, in beta

- Isolated agent per tenant, with per-user identity: TOTP, revocable sessions, audit trail
- Tenant data stays on a self-hosted model; cloud fallback is off and enforced in CI
- Reads Toast POS and supplier data, drafts orders, the owner approves

**GTM engineering**: private

- Sources and scores public-sector leads, infers `fit x intent` from agency documents
- Ministral 3 models on [Modal](https://modal.com)

## Selected work

| Project | What it does | Result |
| --- | --- | --- |
| **[StackWatch](https://github.com/LlamzonAmazon/StackWatch)**<br>`Python` `FastAPI` `ClickHouse` `Semgrep` | Exposure agent. Point it at a domain or repo and it reports what the target runs, which vulnerabilities apply, and which are reachable | Four-rung evidence ladder on every finding: present, reachable, exploitable, confirmed |
| **[Asynchronous Federated Learning](https://github.com/LlamzonAmazon/asynchronous-fl)**<br>`Python` `PyTorch` `Flower` | Layer-wise asynchronous updates for federated learning on health IoT devices. Tested on a 37M-parameter ECG model | **49.7% less client upload**, accuracy 83.2% vs 82.7% for synchronous (3 seeds, p = 0.31) |
| **[Country Development Scoring](https://github.com/PlanCatalyst/TSI-Data-Dashboard)**<br>`Python` `React` `D3` `Azure` | 216 countries, 28 indicators, 35 years, 7 pillars. A Python pipeline publishes to Azure Blob and a React app reads it | **97,038 of 97,038** published values re-derived independently, all matched |
| **[Western Sales Club site and CMS](https://westernsalesclub.ca)**<br>`Next.js` `TypeScript` `Supabase` | Live site and CMS for a student organization. Its executives publish events and sponsors without a developer | **TOTP** enforced in Postgres policies on every admin write |

> [!NOTE]
> StackWatch began as a team build at the SF Tech Week Cyberdefense Hackathon and continued solo. The federated learning work is my thesis, a first-author paper at IEEE GLOBECOM 2026 (Macau, December).

## Background

- **Security Analyst, CYBERWELL** (Apr 2025 to Apr 2026): on call across 7 client tenants, wrote KQL detections, resolved 8+ incidents a day, cut false positives 12%
- **Software Engineer, PlanCatalyst** (Sep 2025 to Apr 2026): built the ingestion pipeline, scoring and publish path for the scoring engine
- **BSc Honours, Computer Science, Western University** (2026): databases, networking, security, algorithms

## Tools

| Area | Tools |
| --- | --- |
| Languages | <img src="assets/badges/python.svg" alt="Python"> <img src="assets/badges/typescript.svg" alt="TypeScript"> <img src="assets/badges/sql.svg" alt="SQL"> <img src="assets/badges/bash.svg" alt="Bash"> <img src="assets/badges/kql.svg" alt="KQL"> |
| Backend and data | <img src="assets/badges/fastapi.svg" alt="FastAPI"> <img src="assets/badges/nodejs.svg" alt="Node.js"> <img src="assets/badges/postgresql.svg" alt="PostgreSQL"> <img src="assets/badges/clickhouse.svg" alt="ClickHouse"> <img src="assets/badges/supabase.svg" alt="Supabase"> <img src="assets/badges/pandas.svg" alt="pandas"> |
| Frontend | <img src="assets/badges/react.svg" alt="React"> <img src="assets/badges/nextjs.svg" alt="Next.js"> <img src="assets/badges/vite.svg" alt="Vite"> <img src="assets/badges/tailwind.svg" alt="Tailwind"> <img src="assets/badges/d3.svg" alt="D3"> |
| Cloud and infra | <img src="assets/badges/cloudflare.svg" alt="Cloudflare"> <img src="assets/badges/aws.svg" alt="AWS"> <img src="assets/badges/azure.svg" alt="Azure"> <img src="assets/badges/terraform.svg" alt="Terraform"> <img src="assets/badges/docker.svg" alt="Docker"> <img src="assets/badges/actions.svg" alt="GitHub Actions"> |
| Security and AI | <img src="assets/badges/semgrep.svg" alt="Semgrep"> <img src="assets/badges/sentinel.svg" alt="Sentinel"> <img src="assets/badges/entra.svg" alt="Entra ID"> <img src="assets/badges/claude.svg" alt="Claude"> <img src="assets/badges/ollama.svg" alt="Ollama"> <img src="assets/badges/pytorch.svg" alt="PyTorch"> |

## DSA practice

NeetCode 150 and LeetCode. The card rebuilds itself from the [solutions repo](https://github.com/LlamzonAmazon/DSA-Problems) on every push.

<a href="https://github.com/LlamzonAmazon/DSA-Problems"><img src="https://raw.githubusercontent.com/LlamzonAmazon/DSA-Problems/main/assets/dsa-progress.svg" alt="DSA progress: NeetCode 150 and LeetCode solved counts" width="760"></a>
