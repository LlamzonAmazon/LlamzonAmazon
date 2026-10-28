<p align="center">
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg"><img src="assets/header-light.svg" alt="Terminal card: Thomas Llamzon, Software Engineer, Security, Agents, Full-Stack, Honours Computer Science (BSc) at Western University, first-author IEEE GLOBECOM 2026" width="100%"></picture>
</p>

<p>
  <a href="https://llamzon.ca"><img src="assets/badges/website.svg" alt="Website"></a>
  <a href="https://www.linkedin.com/in/thomasllamzon"><img src="assets/badges/linkedin.svg" alt="LinkedIn"></a>
  <a href="https://github.com/LlamzonAmazon/asynchronous-fl/blob/main/paper/main-conference.pdf"><img src="assets/badges/paper.svg" alt="IEEE GLOBECOM 2026 paper"></a>
</p>

## Current Projects

**[Trellum](https://trellum.ca)**: Agent platform for restaurants with two pillars: operations, live now, and growth through go-to-market, with a GTM agent planned `IN BETA`

- Isolated agent per tenant, with per-user identity: TOTP, revocable sessions, audit trail
- Tenant data stays on a self-hosted model; cloud fallback is off and enforced in CI
- Reads Toast POS and supplier data, drafts orders, the owner approves

**Learning GTM Engineering**

- Built a platform that sources and scores public-sector agency leads and infers ICP fit and intent from agency documents
- Utilizes [Mistral](https://mistral.ai/) Ministral 3 models on [Modal](https://modal.com)

## Selected work

| Project | What it does | Result |
| --- | --- | --- |
| **[StackWatch](https://github.com/LlamzonAmazon/StackWatch)**<br>`Python` `FastAPI` `ClickHouse` `Semgrep` | An autonomous threat intelligence agent built around an organization's systems and context. Infers threats from code, internet footprint and business context | Ranks each threat by what it would cost the business with the evidence trail attributed with every finding |
| **[Asynchronous Federated Learning](https://github.com/LlamzonAmazon/asynchronous-fl)**<br>`Python` `PyTorch` `Flower` | Layer-wise asynchronous updates for federated learning on health IoT devices. Tested on a 37M-parameter ECG model | **49.7% less client upload**, accuracy 83.2% vs 82.7% for synchronous (3 seeds, p = 0.31) |
| **[Global Country Development Scoring Engine](https://jolly-pebble-0e2f9300f.7.azurestaticapps.net/#/map)**<br>`Python` `Azure` `D3` `React` | Cloud ETL Pipeline ingesting data from 5 public data sources (216 countries, 28 indicators over 35 years creating 7 core development pillars) | **97,053** real values published; the other **114,627** of 211,680 cells are kept as gaps, never scored as zeros |
| **[Western Sales Club site and CMS](https://westernsalesclub.ca)**<br>`Next.js` `TypeScript` `Supabase` | Live site + CMS for Western's Sales Club. Executives can authenticate and log in to their CMS to modify frontend website content in real time. | **TOTP** enforced in Postgres policies on every admin write, RLS enforced, read-only anon grants, append-only admin audit log |

> [!NOTE]
> StackWatch began as a team build at the 2026 SF Tech Week Cyberdefense Hackathon, and I kept building it into an autonomous threat intelligence agent.
> The federated learning work is my thesis. I am the first-author of the paper to be presented at IEEE GLOBECOM 2026 (Macau, December).

## Background

- **Security Analyst, CYBERWELL** (Sep 2025 to Apr 2026; Security Operations Intern from Apr 2025)
- **Software Engineer, PlanCatalyst (Plan International Canada)** (Sep 2025 to Apr 2026)
- **BSc Honours, Computer Science, Western University** (2026)

## Tools

| Area | Tools |
| --- | --- |
| Languages | <img src="assets/badges/python.svg" alt="Python"> <img src="assets/badges/typescript.svg" alt="TypeScript"> <img src="assets/badges/sql.svg" alt="SQL"> <img src="assets/badges/bash.svg" alt="Bash"> <img src="assets/badges/kql.svg" alt="KQL"> |
| Backend and data | <img src="assets/badges/fastapi.svg" alt="FastAPI"> <img src="assets/badges/nodejs.svg" alt="Node.js"> <img src="assets/badges/postgresql.svg" alt="PostgreSQL"> <img src="assets/badges/clickhouse.svg" alt="ClickHouse"> <img src="assets/badges/supabase.svg" alt="Supabase"> <img src="assets/badges/pandas.svg" alt="pandas"> |
| Frontend | <img src="assets/badges/react.svg" alt="React"> <img src="assets/badges/nextjs.svg" alt="Next.js"> <img src="assets/badges/vite.svg" alt="Vite"> <img src="assets/badges/tailwind.svg" alt="Tailwind"> <img src="assets/badges/d3.svg" alt="D3"> |
| Cloud and infra | <img src="assets/badges/cloudflare.svg" alt="Cloudflare"> <img src="assets/badges/aws.svg" alt="AWS"> <img src="assets/badges/azure.svg" alt="Azure"> <img src="assets/badges/terraform.svg" alt="Terraform"> <img src="assets/badges/docker.svg" alt="Docker"> <img src="assets/badges/actions.svg" alt="GitHub Actions"> |
| Security and AI | <img src="assets/badges/semgrep.svg" alt="Semgrep"> <img src="assets/badges/sentinel.svg" alt="Sentinel"> <img src="assets/badges/entra.svg" alt="Entra ID"> <img src="assets/badges/ollama.svg" alt="Ollama"> <img src="assets/badges/pytorch.svg" alt="PyTorch"> |

## DSA practice

NeetCode 150 and LeetCode. The card rebuilds itself from the [solutions repo](https://github.com/LlamzonAmazon/DSA-Problems) on every push.

<a href="https://github.com/LlamzonAmazon/DSA-Problems"><img src="https://raw.githubusercontent.com/LlamzonAmazon/DSA-Problems/main/assets/dsa-progress.svg" alt="DSA progress: NeetCode 150 and LeetCode solved counts" width="760"></a>
