# Source provenance and publication boundary

<!-- clean-docs:purpose -->
This portfolio piece recomposes two author-owned public sources without importing private task data or agent transcripts.
<!-- clean-docs:end purpose -->


## Public enforcement source

- Repository: `owieschon/agent-governance-lab`
- Pinned source commit: `218d2dab8ebfa9c6e7a19f065e4a104b94d272d3`
- Relevant surfaces: `rails/verifier/verify.sh`, the protected manifest/oracle/freshness
  checks, and `rails/adversarial/run_eval.sh` with its planted violation cases.

`src/trustladder/governance/gate.py` models only the treatment semantics the experiment
needs: written rules, a visible nonblocking gate, and the same gate with release authority.
It is not presented as a copy or replacement for the full verifier. Scheduled extended CI
runs the actual public mechanism at the pinned commit.

## Public measurement source

- Repository working title: TrustLadder (`code_ver` remote)
- Foundation commit: `e1fc744ded1c4ebd532032c0d20d826538f68d5e`
- Relevant surfaces: signed run-records, blind grading, calibration, validity gates,
  confirmatory analysis, and the repaired record-to-grade seam.

## Excluded private material

- the original task battery and answer keys;
- raw agent transcripts, machine paths, and session identifiers;
- the full private preregistration/deviation log;
- any private governance-kit implementation.

The statement that Stage 1 collected 72 runs and stopped before grading is a sanitized
historical observation, not a publicly reproducible result. The public artifact proves the
mechanism semantics, integrity refusals, analysis order, and synthetic pipeline behavior. It
does not claim an empirical treatment effect on real agents.
