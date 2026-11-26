<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="Harjeet J L, Cloud Engineer, DevOps and CloudOps" src="assets/banner-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://linkedin.com/in/harjeet-jl"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-harjeet--jl-0A66C2?style=flat-square&logo=linkedin&logoColor=white"></a>
  <a href="https://linktr.ee/harjeet_jl"><img alt="Linktree" src="https://img.shields.io/badge/Linktree-harjeet__jl-43E55E?style=flat-square&logo=linktree&logoColor=white"></a>
  <a href="https://twitter.com/HarjeetJl"><img alt="X" src="https://img.shields.io/badge/X-@HarjeetJl-000000?style=flat-square&logo=x&logoColor=white"></a>
  <img alt="Location" src="https://img.shields.io/badge/Chennai%20%C2%B7%20Hyderabad-India-FF9900?style=flat-square">
</p>

Cloud Engineer at **KFin Technologies**, working on DevOps and CloudOps for a regulated
financial-services platform on AWS. I turn manual release and provisioning work into
self-service automation: Jenkins pipelines, dynamic Terraform, containers on ECS and EKS,
and the internal tools that keep them healthy. I'm also on the 24/7 production support team.

## Impact

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/impact-dark.svg">
  <img alt="2,000+ production deployments, 44 AWS accounts, build and deploy cut from 6 hours to 5-7 minutes, 42k+ resources in the largest account" src="assets/impact-light.svg" width="100%">
</picture>

## How I ship

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/pipeline-dark.svg">
  <img alt="Release pipeline: git push to Gitea, Jenkins tests, Docker build, Terraform provisioning, deploy to ECS or EKS, health checks" src="assets/pipeline-light.svg" width="100%">
</picture>

Every application gets its own Jenkins pipeline wired to Gitea: tests on every push, Docker
images built and pushed, ECS task definitions and services updated, and the rollout watched
until it is healthy. Infrastructure comes from Terraform modules parameterized from Jenkins,
so teams create resources without touching YAML or `.tf` files.

## What I've built

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/project-buildforge-dark.svg">
  <img alt="BuildForge: AI failure analysis plugin for Jenkins, built with Java, Python and an MCP agent" src="assets/project-buildforge-light.svg" width="49%">
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/project-waf-platform-dark.svg">
  <img alt="Centralized AWS WAF monitoring platform across 44 accounts, built with Lambda, Step Functions, FastAPI and ECS Fargate" src="assets/project-waf-platform-light.svg" width="49%">
</picture>

Both are internal tools at KFin, so the code isn't public. Open source work:

| Project | About |
|---|---|
| [harjeetjl-portfolio](https://github.com/Harjeet2411/harjeetjl-portfolio) | My interactive 3D portfolio, [live on GitHub Pages](https://harjeet2411.github.io/harjeetjl-portfolio/) |
| [gha-pinner](https://github.com/Harjeet2411/gha-pinner) | Pins GitHub Actions to commit SHAs and fails CI when one is left on a movable tag |
| [cert-watch](https://github.com/Harjeet2411/cert-watch) | Checks TLS certificate expiry, weak ciphers and old TLS versions for a list of hosts and exits non-zero so CI can fail before a certificate lapses |
| [tf-drift-report](https://github.com/Harjeet2411/tf-drift-report) | Turns `terraform show -json` plan output into a short drift report, with destroys and replaces listed first and sensitive values never printed |
| [k8s-cost-peek](https://github.com/Harjeet2411/k8s-cost-peek) | Prices Kubernetes CPU and memory requests per namespace or team from `kubectl` output, with a CI budget check |
| [dockerfile-doctor](https://github.com/Harjeet2411/dockerfile-doctor) | Dockerfile security and image-size linter with fix suggestions and SARIF output |
| [waflens](https://github.com/Harjeet2411/waflens) | Summarises ModSecurity/Coraza WAF audit logs and flags likely false positives |
| [Rag-Api-with-FAST-API](https://github.com/Harjeet2411/Rag-Api-with-FAST-API) | RAG API over my profile: ChromaDB retrieval, local Ollama model, FastAPI endpoints with multi-user documents |
| [Rag-Api-Ollama](https://github.com/Harjeet2411/Rag-Api-Ollama) | Run LLMs locally with Ollama, plus a custom coding-tutor model built from a Modelfile |
| [Hukum-AI-Video-Editor](https://github.com/Harjeet2411/Hukum-AI-Video-Editor) | AI-assisted video editor |
| [Capstone-Devops](https://github.com/Harjeet2411/Capstone-Devops) | DevOps capstone: pipeline, containers and infrastructure end to end |
| [DSA-Visualizer](https://github.com/Harjeet2411/DSA-Visualizer) | Interactive data structures and algorithms visualizer |
| [Mouse-Gestures-with-OpenCV](https://github.com/Harjeet2411/Mouse-Gestures-with-Open-Cv-Hand-Gestures-) | Control the mouse with hand gestures using OpenCV |
| [ARQE-Flutter-App](https://github.com/Harjeet2411/ARQE-Flutter-App) | Flutter mobile app |

## Toolbox

**Cloud** &nbsp;
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=FF9900)
![ECS](https://img.shields.io/badge/ECS-FF9900?style=for-the-badge&logo=amazonecs&logoColor=white)
![EKS](https://img.shields.io/badge/EKS-FF9900?style=for-the-badge&logo=amazoneks&logoColor=white)
![Lambda](https://img.shields.io/badge/Lambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white)
![CloudFront](https://img.shields.io/badge/CloudFront-8C4FFF?style=for-the-badge&logo=amazonaws&logoColor=white)

**IaC & CI/CD** &nbsp;
![Terraform](https://img.shields.io/badge/Terraform-844FBA?style=for-the-badge&logo=terraform&logoColor=white)
![CloudFormation](https://img.shields.io/badge/CloudFormation-E7157B?style=for-the-badge&logo=amazonaws&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Gitea](https://img.shields.io/badge/Gitea-609926?style=for-the-badge&logo=gitea&logoColor=white)

**Containers & ops** &nbsp;
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)

**Code** &nbsp;
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Bash](https://img.shields.io/badge/Shell-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)

## On GitHub

<table>
  <tr>
    <td width="50%">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Harjeet2411/Harjeet2411/output/stats-dark.svg">
        <img alt="GitHub activity: contributions, commits, streak and public repos" src="https://raw.githubusercontent.com/Harjeet2411/Harjeet2411/output/stats-light.svg" width="100%">
      </picture>
    </td>
    <td width="50%">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Harjeet2411/Harjeet2411/output/languages-dark.svg">
        <img alt="Top languages in public repositories" src="https://raw.githubusercontent.com/Harjeet2411/Harjeet2411/output/languages-light.svg" width="100%">
      </picture>
    </td>
  </tr>
</table>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Harjeet2411/Harjeet2411/output/snake-dark.svg">
  <img alt="Contribution graph being eaten by a snake" src="https://raw.githubusercontent.com/Harjeet2411/Harjeet2411/output/snake-light.svg" width="100%">
</picture>

### Recently

<!-- ACTIVITY:START -->
**Week of 23 Nov 2026**
- Built cert-watch, the sixth weekly tool: checks TLS certificate expiry for a list of hosts, flags refused certificates, weak ciphers and servers that still accept TLS 1.0 or 1.1, and exits non-zero so CI can fail before a certificate lapses. It is now published as [cert-watch](https://github.com/Harjeet2411/cert-watch).

**Week of 16 Nov 2026**
- Built tf-drift-report, the fifth weekly tool: turns `terraform show -json` plan output into a short drift report (text or a Markdown pull request comment), lists what will be destroyed or replaced with databases and buckets first, never prints sensitive values and can fail CI on drift or destroys. It is now published as [tf-drift-report](https://github.com/Harjeet2411/tf-drift-report).
- The algorithm visualizer's interactive canvas now redraws when its edges change, and three unused dependencies (zod, react-query, hookform resolvers) were removed. EaseMySSH shows an error instead of failing silently when Edit servers, Reload or Logs cannot run, and its CI workflow pins its actions to commit SHAs.
- The algorithm visualizer lost over 1,300 lines of unused components, got `typecheck` and `lint` scripts, and its learning roadmap no longer rebuilds its static algorithm lists on every render. EaseMySSH now disposes the graphics objects behind its tray icons and shares one tooltip across rows instead of making one per row on every reload.
- The algorithm visualizer's graph canvas now redraws when its size changes, and its algorithm runner resets on a stable dependency list instead of an incomplete one.
- The algorithm visualizer's graph pages now number their exploration steps from the latest list, so a stale render can no longer repeat a step number.

<!-- ACTIVITY:END -->

### Weekly build

<!-- WEEKLY:START -->
Every week I build a small open-source DevSecOps tool. Shipped so far: [waflens](https://github.com/Harjeet2411/waflens) (WAF audit-log analyzer that flags likely false positives), [dockerfile-doctor](https://github.com/Harjeet2411/dockerfile-doctor) (Dockerfile security and image-size linter), [k8s-cost-peek](https://github.com/Harjeet2411/k8s-cost-peek) (Kubernetes request costs per namespace or team) and [gha-pinner](https://github.com/Harjeet2411/gha-pinner) (pins GitHub Actions to commit SHAs) [tf-drift-report](https://github.com/Harjeet2411/tf-drift-report) (Terraform plan drift summary) and [cert-watch](https://github.com/Harjeet2411/cert-watch) (TLS certificate expiry checks).
<!-- WEEKLY:END -->

---

<p align="center"><sub>B.Tech CSE (AI &amp; ML), SRIHER Chennai · AWS Academy Cloud Foundations and ML Foundations<br>
Cards are generated daily by <a href=".github/workflows/profile.yml">a workflow in this repo</a>.</sub></p>
