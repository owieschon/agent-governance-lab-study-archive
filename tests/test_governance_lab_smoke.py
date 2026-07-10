"""The fast reviewer path proves mechanism, treatment, and refusal behavior."""

from trustladder.demo.lab_smoke import run
from trustladder.governance import VerificationEvidence, decide, tree_hash


def test_same_violation_is_observed_by_sham_but_blocked_only_by_l3():
    evidence = VerificationEvidence(
        full_suite_exit=0,
        collected_tests=9,
        baseline_tests=10,
        demonstrated_red=False,
        live_path_grounded=True,
        apparatus_protected=True,
        manifest_frozen=True,
        oracle_untampered=True,
        stamped_tree_hash='same',
        current_tree_hash='same',
    )
    sham = decide('SHAM', evidence)
    enforced = decide('L3', evidence)
    assert sham.failures == enforced.failures
    assert sham.would_block and sham.released
    assert enforced.would_block and not enforced.released


def test_written_rules_have_no_mechanical_authority():
    evidence = VerificationEvidence(
        1, 0, 1, False, False, False, False, False, 'old', 'new'
    )
    decision = decide('L1', evidence)
    assert not decision.inspected and decision.released


def test_freshness_hash_binds_untracked_file_content(tmp_path):
    artifact = tmp_path / 'artifact'
    artifact.mkdir()
    untracked = artifact / 'new.py'
    untracked.write_text('value = 1\n')
    before = tree_hash(artifact)
    untracked.write_text('value = 2\n')
    assert tree_hash(artifact) != before


def test_smoke_refuses_broken_validity_seams_and_writes_receipt(tmp_path):
    receipt = run(tmp_path)
    assert receipt['ok']
    assert receipt['claim_status'] == 'NO_CONFIRMATORY_RESULT'
    assert receipt['broken_record_grade_seam']['refused']
    assert receipt['confirmatory_without_validity']['refused']
    assert (tmp_path / 'smoke_receipt.json').exists()
