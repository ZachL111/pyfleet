# Pyfleet Walkthrough

The fixture is intentionally compact, so the review starts with the cases that pull farthest apart.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | quorum health | 183 | ship |
| stress | lease drift | 152 | ship |
| edge | replica lag | 184 | ship |
| recovery | membership churn | 190 | ship |
| stale | quorum health | 257 | ship |

Start with `stale` and `stress`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

If `stress` becomes less cautious without a clear reason, I would inspect the drag input first.
