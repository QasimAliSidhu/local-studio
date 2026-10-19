# Proposed enterprise roadmap

Status: planning only. The current release is a personal local learning workspace. This document describes how a separate shared product could be developed; it does not represent a deployed enterprise service or a delivery-date commitment.

## 1. Establish organization and learner boundaries

Introduce organization membership, individual learner records, instructor and administrator roles, and organization-scoped storage for code, progress, notes, assessments and tutor history. Integrate enterprise single sign-on through an identity provider rather than sharing the personal owner's login. Version course content and database migrations.

Acceptance: two organizations and two learner accounts exercise every read/write path, including files, asynchronous jobs and exports; attempts to access another account's resources are denied. Instructor access matches assigned cohorts.

## 2. Separate execution and AI from the application

Place Run and Submit behind a queue and disposable isolated workers. Evaluate a sandbox runtime or microVM against the Python/Go lesson workload. Enforce CPU, memory, process, wall-time, disk and output limits outside learner code. Restrict network access, separate per-run files and keep application/provider secrets out of workers. Clean up completed and interrupted jobs.

Use an organization-aware server-side AI integration with its own credentials, usage quotas and data controls. The personal Codex session in the local app is not the shared platform's credential model.

Acceptance: an infinite loop, resource-heavy run and interrupted job terminate within policy; one run cannot read another's files or application secrets. Per-team runner and AI usage can be limited and measured.

## 3. Build the teaching workflow

Add cohort enrollment, assignments, instructor feedback, versioned assessments and progress dashboards. Preserve the exact assignment/test version associated with a submission. Check accessibility with keyboard navigation and assistive technology, as well as phone layouts.

Acceptance: an instructor can assign a course, review the intended learners' work and interpret progress without accessing unrelated learners. Existing submissions keep their original assessment context after a course revision.

## 4. Prove operational readiness

Add audit events, monitored application and worker services, release rollback, dependency maintenance, retention controls and authorized data export/deletion. Agree pilot recovery and availability targets before making service commitments. Test backup restores and concurrent learners against a specified workload, with runner queue time and AI costs visible.

Acceptance: recover the selected learner/organization in an isolated restore exercise, verify access boundaries and test the agreed pilot concurrency. Record the actual result and capacity limits.

## 5. Run a small team pilot before expanding

Start with one team and a defined learning goal. Measure first-lesson completion, pre/post assessment change, learner return rate, support requests, runner failures and cost per active learner. Collect learner and instructor feedback. Prioritize the next release from that evidence before adding billing, LMS integrations or broader provisioning.

Acceptance: pilot outcomes, known issues, operating costs and the next scope are reviewed with the team. Expansion follows demonstrated learning value and working isolation/recovery controls.

## Planning references

- [OWASP Multi-Tenant Application Security](https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html): boundaries across identity, data, files, jobs, audit and restoration.
- [gVisor Security Model](https://gvisor.dev/docs/architecture_guide/security/): sandbox boundaries and the external resource/network controls still required. gVisor is a candidate to evaluate, not a dependency claimed by this release.

Hosting, deployment changes, paid infrastructure and production commitments require a separately scoped implementation. This repository release does not change the original personal installation.
