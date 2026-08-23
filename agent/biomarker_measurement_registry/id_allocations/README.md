# Registry Numeric-ID Allocations

Status: Founder Approved Storage and Naming Convention / Record Creation Not Authorized

This directory stores immutable, machine-readable numeric-ID allocation ledgers. Allocation ledgers are separate from Registry records and from the Candidate Ledger.

A proposed reservation becomes effective only after Founder approval of the allocation ledger's exact SHA and a controlled Git commit. Uncommitted or Founder-review-pending proposals are not effective reservations.

Allocation is namespace-level, monotonic, non-semantic, and never reused. IDs do not encode body system, Pilot, priority, dependency, clinical meaning, lifecycle, or product grouping. Allocated, reserved, or abandoned IDs must not be reassigned.

Legacy review coordinates are collision-reserved to prevent audit ambiguity. They are not formal Registry IDs and do not gain Registry authority, but their strings must not be reused.

The Candidate Ledger remains unchanged during allocation.

## Effective Reservation Source of Truth

An effective reservation requires both:

1. a committed allocation ledger; and
2. a committed Founder approval closeout naming that ledger's exact SHA.

A reviewed proposal may retain embedded `Draft`, `effective_reserved_id_count: 0`, or `effective_reservation: false` fields in order to preserve the exact reviewed bytes. After the required exact-SHA approval and controlled Git commit, the committed Founder approval closeout is authoritative for reservation effectiveness.

Future ID inventory audits must inspect both the committed allocation ledger and its exact-SHA Founder approval closeout. This README does not hard-code a mutable reservation count.
