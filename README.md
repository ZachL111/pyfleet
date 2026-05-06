# pyfleet

`pyfleet` keeps a focused Python implementation around distributed systems. The project goal is to schedule workloads onto heterogeneous nodes with bin-packing and drain plans.

## Use Case

This is intentionally local and self-contained so it can be inspected without credentials, services, or seeded history.

## Pyfleet Review Notes

`stale` and `stress` are the cases worth reading first. They show the optimistic and cautious ends of the fixture.

## Highlights

- `fixtures/domain_review.csv` adds cases for quorum health and lease drift.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/pyfleet-walkthrough.md` walks through the case spread.
- The Python code includes a review path for `quorum health` and `lease drift`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Code Layout

The fixture data drives the tests. The code stays thin, while `metadata/domain-review.json` and `config/review-profile.json` explain what each case is meant to protect.

The added Python path is deliberately direct, with fixtures doing most of the explaining.

## Run The Check

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Regression Path

The same command runs the local verification path. The highest-scoring domain case is `stale` at 257, which lands in `ship`. The most cautious case is `stress` at 152, which lands in `ship`.

## Future Work

The repository is intentionally scoped to local checks. I would expand it by adding adversarial fixtures before adding features.
