Branching Strategy & Workflow

This document defines the Git branching model for the Rubber Molding IoT Project.
The goal is to maintain clean, stable, and well-organized development.

1. Required Branches
  
1. main (Production Branch)

Contains production-ready and stable code.

No one is allowed to push directly.

Only Pull Requests from the dev branch are merged here.

Protected branch.

2. dev (Development / Integration Branch)

Main working branch for the team.

All features are merged here after review.

Used for:

Internal testing

Integrating new components

QA validation

All feature branches → merge into dev first.

3. feature/* (Task-Level Branches)

Each task or module must have its own branch.

Examples:

feature/simulator

feature/ml-training

feature/frontend-dashboard

feature/backend-api

feature/ingestion-pipeline

feature/predictive-maintenance-model

Naming Rule:

feature/<clear-task-name>

4. Workflow (Step-by-Step)
Step 1 — Developer works locally

Developer creates a new feature branch:

git checkout -b feature/<feature-name>


Example:

git checkout -b feature/simulator

Step 2 — Developer pushes work
git push origin feature/<feature-name>

Step 3 — Create Pull Request → dev

Every feature branch must be merged only through a PR.

PR Target:

feature/*  →  dev

Step 4 — Review by Tech Leads

The Tech Leads check:

Code quality

Follows coding standards

No breaking changes

Works as expected

Once approved → merge into dev.

Step 5 — Testing on dev

QA/Testers validate:

Pipeline flow

Simulator output

ML modules

Backend endpoints

UI dashboards

If all tests pass → Tech Leads proceed.

Step 6 — Merge dev → main

A final PR is created:

dev  →  main


This PR requires:

Full review

Final approval

Passing CI/CD

Once merged → production release.

Branch Flow Diagram (Simple)
feature/*  →  dev  →  main

5. Summary
Branch	Purpose	Rules
main	Production-ready code	Only merges from dev, protected
dev	Integration/testing code	All features merge here
feature/*	Developer work branches	One branch per task
