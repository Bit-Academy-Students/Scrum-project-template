# Bescherm `main`

Maak in elke publieke teamrepository een actieve branch ruleset voor de default branch (`main`). Repository rulesets zijn beschikbaar voor publieke repositories.

## Aanbevolen regels

- Target branches: include default branch.
- Require a pull request before merging.
- Require 1 approving review.
- Require review-thread resolution before merging.
- Require status checks to pass before merging zodra het project relevante CI-checks heeft.
- Block force pushes.
- Block branch deletion.
- Laat alleen docenten/beheerders een bypass gebruiken; studenten werken via pull requests.

De ruleset wordt niet meegekopieerd wanneer GitHub een repository vanuit deze template maakt. Daarom staat dit document bewust als onderdeel van de beheerderschecklist.
