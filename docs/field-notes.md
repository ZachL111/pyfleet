# Field Notes

I would read this project from the data inward: cases first, implementation second.

The domain cases cover `quorum health`, `lease drift`, `replica lag`, and `membership churn`. They sit beside the smaller starter fixture so the project has both a compact scoring check and a domain-flavored review check.

The model rewards signal and confidence, then pulls back for drag. In this fixture, `stress` shows where that pullback matters most.

The point is not to make the repository bigger. The point is to make the important judgment testable.
