<p align="center">
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg"><img src="assets/header-light.svg" alt="Terminal card: thomas@llamzon, Forward Deployed Engineer, security and full-stack, BSc Honours CS at Western University, first-author IEEE GLOBECOM 2026" width="100%"></picture>
</p>

<p>
  <a href="https://llamzon.ca"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/buttons/website-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/buttons/website-light.svg"><img src="assets/buttons/website-light.svg" alt="Website"></picture></a>
  <a href="https://www.linkedin.com/in/thomasllamzon"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/buttons/linkedin-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/buttons/linkedin-light.svg"><img src="assets/buttons/linkedin-light.svg" alt="LinkedIn"></picture></a>
  <a href="https://github.com/LlamzonAmazon/asynchronous-fl/blob/main/paper/main-conference.pdf"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/buttons/paper-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/buttons/paper-light.svg"><img src="assets/buttons/paper-light.svg" alt="IEEE GLOBECOM 2026 paper"></picture></a>
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
| Languages | <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/python-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/python-light.svg"><img src="assets/labels/python-light.svg" alt="Python"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/typescript-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/typescript-light.svg"><img src="assets/labels/typescript-light.svg" alt="TypeScript"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/sql-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/sql-light.svg"><img src="assets/labels/sql-light.svg" alt="SQL"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/bash-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/bash-light.svg"><img src="assets/labels/bash-light.svg" alt="Bash"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/kql-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/kql-light.svg"><img src="assets/labels/kql-light.svg" alt="KQL"></picture> |
| Backend and data | <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/fastapi-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/fastapi-light.svg"><img src="assets/labels/fastapi-light.svg" alt="FastAPI"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/nodejs-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/nodejs-light.svg"><img src="assets/labels/nodejs-light.svg" alt="Node.js"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/postgresql-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/postgresql-light.svg"><img src="assets/labels/postgresql-light.svg" alt="PostgreSQL"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/clickhouse-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/clickhouse-light.svg"><img src="assets/labels/clickhouse-light.svg" alt="ClickHouse"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/supabase-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/supabase-light.svg"><img src="assets/labels/supabase-light.svg" alt="Supabase"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/pandas-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/pandas-light.svg"><img src="assets/labels/pandas-light.svg" alt="pandas"></picture> |
| Frontend | <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/react-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/react-light.svg"><img src="assets/labels/react-light.svg" alt="React"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/nextjs-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/nextjs-light.svg"><img src="assets/labels/nextjs-light.svg" alt="Next.js"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/vite-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/vite-light.svg"><img src="assets/labels/vite-light.svg" alt="Vite"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/tailwind-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/tailwind-light.svg"><img src="assets/labels/tailwind-light.svg" alt="Tailwind"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/d3-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/d3-light.svg"><img src="assets/labels/d3-light.svg" alt="D3"></picture> |
| Cloud and infra | <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/cloudflare-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/cloudflare-light.svg"><img src="assets/labels/cloudflare-light.svg" alt="Cloudflare"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/aws-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/aws-light.svg"><img src="assets/labels/aws-light.svg" alt="AWS"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/azure-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/azure-light.svg"><img src="assets/labels/azure-light.svg" alt="Azure"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/terraform-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/terraform-light.svg"><img src="assets/labels/terraform-light.svg" alt="Terraform"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/docker-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/docker-light.svg"><img src="assets/labels/docker-light.svg" alt="Docker"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/actions-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/actions-light.svg"><img src="assets/labels/actions-light.svg" alt="GitHub Actions"></picture> |
| Security and AI | <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/semgrep-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/semgrep-light.svg"><img src="assets/labels/semgrep-light.svg" alt="Semgrep"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/sentinel-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/sentinel-light.svg"><img src="assets/labels/sentinel-light.svg" alt="Sentinel"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/entra-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/entra-light.svg"><img src="assets/labels/entra-light.svg" alt="Entra ID"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/claude-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/claude-light.svg"><img src="assets/labels/claude-light.svg" alt="Claude"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/ollama-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/ollama-light.svg"><img src="assets/labels/ollama-light.svg" alt="Ollama"></picture> <picture><source media="(prefers-color-scheme: dark)" srcset="assets/labels/pytorch-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/labels/pytorch-light.svg"><img src="assets/labels/pytorch-light.svg" alt="PyTorch"></picture> |

## DSA practice

NeetCode 150 and LeetCode. The card rebuilds itself from the [solutions repo](https://github.com/LlamzonAmazon/DSA-Problems) on every push.

<a href="https://github.com/LlamzonAmazon/DSA-Problems"><img src="https://raw.githubusercontent.com/LlamzonAmazon/DSA-Problems/main/assets/dsa-progress.svg" alt="DSA progress: NeetCode 150 and LeetCode solved counts" width="760"></a>
