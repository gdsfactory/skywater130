# [Changelog](https://keepachangelog.com/en/1.0.0/)

<!-- towncrier release notes start -->

## [1.0.0](https://github.com/gdsfactory/skywater130/releases/tag/v1.0.0) - 2026-04-27

First stable release. Marks API parity with the upstream Magic Tcl pcell generators
and a stable public surface for downstream tools.

### Breaking

- Major refactor: ported electrical pcells from Magic Tcl generators with XOR-validated parity ([#157](https://github.com/gdsfactory/skywater130/pull/157))
  - Replaces the legacy per-device pcell modules (`nmos.py`, `nmos_5v.py`, `pmos.py`, `mimcap_1.py`, `mimcap_2.py`, …) with consolidated modules under `sky130/pcells/` (`mosfets.py`, `bjts.py`, `capacitors.py`, `diodes.py`, `esd.py`, `guard_ring.py`, `contact.py`).
  - Adds `sky130.logic` and `sky130.fixed` cell collections.
  - Removes legacy top-level `sky130/nmos.py` shim that shadowed `sky130.pcells.nmos` ([#174](https://github.com/gdsfactory/skywater130/pull/174)).
  - Bumps minimum Python to `>=3.12`.
- Routing + port mapping rework for gdsfactory+ integration ([#135](https://github.com/gdsfactory/skywater130/pull/135), [#151](https://github.com/gdsfactory/skywater130/pull/151)).

### New

- `@cell` type tags on all components ([#170](https://github.com/gdsfactory/skywater130/pull/170)).
- DRC workflow + numeric DRC badge ([#154](https://github.com/gdsfactory/skywater130/pull/154), [#169](https://github.com/gdsfactory/skywater130/pull/169)).
- Metric badge workflows + README dashboard ([#168](https://github.com/gdsfactory/skywater130/pull/168)).
- Magic-batch reference generator + parameter sweeps for XOR test infrastructure (`scripts/magic/`).

### Fixes

- `build_cell.py`: port `all_cells` aggregator from IHP template; restore green DRC ([#174](https://github.com/gdsfactory/skywater130/pull/174)).
- `sky130/circuits/sample.pic.yml`: switch routing to `route_bundle` ([#174](https://github.com/gdsfactory/skywater130/pull/174)).
- Docs build, pre-commit, dependency resolution ([#155](https://github.com/gdsfactory/skywater130/pull/155)).
- Hide private repo links from public docs ([#153](https://github.com/gdsfactory/skywater130/pull/153)).

### Maintenance

- Sync drift-enforced workflow templates from upstream (`pages.yml`, `dependabot.yml`, `release-drafter.yml`, `test_code.yml`, `issue.yml`, `claude-pr-review.yml`) ([#172](https://github.com/gdsfactory/skywater130/pull/172), [#173](https://github.com/gdsfactory/skywater130/pull/173)).
- Switch dependabot to `uv` ecosystem with cooldown ([#156](https://github.com/gdsfactory/skywater130/pull/156), [#163](https://github.com/gdsfactory/skywater130/pull/163)).
- Bump `gdsfactory` to `~=9.40.1` ([#166](https://github.com/gdsfactory/skywater130/pull/166)).
- Bump `release-drafter/release-drafter` 6 → 7.1.1 ([#159](https://github.com/gdsfactory/skywater130/pull/159)).
- Bump `actions/deploy-pages` 4 → 5 ([#161](https://github.com/gdsfactory/skywater130/pull/161)).
- Revert "Migrate CI to centralised pdk-ci-workflow" ([#150](https://github.com/gdsfactory/skywater130/pull/150)).


## [0.15.2](https://github.com/gdsfactory/skywater130/releases/tag/v0.15.2) - 2025-11-07

- Bump astral-sh/setup-uv from 6 to 7 [#125](https://github.com/gdsfactory/skywater130/pull/125)
- Bump actions/setup-python from 5 to 6 [#122](https://github.com/gdsfactory/skywater130/pull/122)
- update docs [#126](https://github.com/gdsfactory/skywater130/pull/126)
- update dmove to move [#124](https://github.com/gdsfactory/skywater130/pull/124)
- update docs [#126](https://github.com/gdsfactory/skywater130/pull/126)
- Bump astral-sh/setup-uv from 6 to 7 [#125](https://github.com/gdsfactory/skywater130/pull/125)
- Bump actions/setup-python from 5 to 6 [#122](https://github.com/gdsfactory/skywater130/pull/122)


## [0.15.1](https://github.com/gdsfactory/skywater130/releases/tag/v0.15.1) - 2025-09-14

- better type annotations and update to gdsfactory 9.15.0 [#121](https://github.com/gdsfactory/skywater130/pull/121)

## [0.15.0](https://github.com/gdsfactory/skywater130/releases/tag/v0.15.0) - 2025-06-08

- add routing strategies


## [0.14.1](https://github.com/gdsfactory/skywater130/releases/tag/v0.14.1) - 2025-06-06

No significant changes.


## [0.14.0](https://github.com/gdsfactory/skywater130/releases/tag/v0.14.0) - 2025-06-06

No significant changes.


## [0.13.1](https://github.com/gdsfactory/skywater130/releases/tag/v0.13.1) - 2025-03-16

No significant changes.


## [0.13.0](https://github.com/gdsfactory/skywater130/releases/tag/v0.13.0) - 2025-02-25

- Migrate code to gdsfactory9 [#104](https://github.com/gdsfactory/skywater130/pull/104)


## [0.12.2](https://github.com/gdsfactory/skywater130/releases/tag/v0.12.2) - 2024-07-15

No significant changes.


## [0.12.1](https://github.com/gdsfactory/skywater130/releases/tag/v0.12.1) - 2024-06-29

- Update gdsfactory840 [#99](https://github.com/gdsfactory/skywater130/pull/99)

## [0.12.0](https://github.com/gdsfactory/skywater130/releases/tag/v0.12.0) - 2024-06-25

No significant changes.


## [0.11.1](https://github.com/gdsfactory/skywater130/releases/tag/v0.11.1) - 2024-05-12

No significant changes.


## [0.11.0](https://github.com/gdsfactory/skywater130/releases/tag/v0.11.0) - 2024-05-09

No significant changes.


## [0.10.1](https://github.com/gdsfactory/skywater130/releases/tag/v0.10.1) - 2024-03-04

No significant changes.


## [0.10.0](https://github.com/gdsfactory/skywater130/releases/tag/v0.10.0) - 2024-03-04

No significant changes.


## [0.9.0](https://github.com/gdsfactory/skywater130/releases/tag/v0.9.0) - 2023-11-18

- update to gdsfactory 7.8.17

## [0.8.0](https://github.com/gdsfactory/skywater130/compare/v0.8.0...v0.7.0)

- update to gdsfactory 7.3.0

## 0.7.0

- update to gdsfactory 6.42.0 [PR](https://github.com/gdsfactory/skywater130/pull/60)
- nice YAML based layer_views

## 0.5.0

- update to gdsfactory 6.37.3 [PR](https://github.com/gdsfactory/skywater130/pull/58)

## 0.4.0

- update to gdsfactory 6.20.5

## 0.3.0

- update to gdsfactory 6.16.2

## 0.2.0

- update to gdsfactory 6.0.1

## 0.1.0

- update to gdsfactory 5.41.0
- added Pcells

## [0.0.13](https://github.com/gdsfactory/skywater130/pull/31)

- update to gdsfactory 5.12.13
- add docs

## [0.0.11](https://github.com/gdsfactory/skywater130/pull/14)

- add spice models

## 0.0.9

- update to gdsfactory 5.9.0

## [0.0.7](https://github.com/gdsfactory/skywater130/pull/2)

- update to gdsfactory 5.8.8


## 0.0.5

- update to gdsfactory 5.4.2
