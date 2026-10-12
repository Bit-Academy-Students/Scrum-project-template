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

De ruleset wordt niet meegekopieerd wanneer GitHub een repository vanuit deze template maakt. Importeer hem daarom na het aanmaken van elke nieuwe repository vanuit deze template.

## Ruleset importeren

1. Open de nieuwe repository op GitHub → **Settings** → **Rules** → **Rulesets**.
2. Kies **New ruleset** → **Import a ruleset**.
3. Selecteer [`main_branch_protection.json`](./main_branch_protection.json) uit deze map.
4. Controleer dat **Enforcement status** op *Active* staat en kies **Create**.

Het bestand bevat: pull request met 1 approval (extra approval bij unattributed changes, zodat een Copilot-review zonder auteur de approval niet kan vervangen), stale reviews dismissen bij nieuwe pushes, review-threads oplossen, verplichte status check `ci` (branch moet up-to-date zijn), geen force pushes, geen branch deletion. Repository admins mogen bypassen.

## Status check `ci` instellen

De ruleset eist een check met de naam `ci`. Zolang geen workflow die check rapporteert, blokkeert GitHub elke merge ("Expected - Waiting for status to be reported"). Zorg dus voor:

1. Een workflow in `.github/workflows/` met trigger `on: pull_request` (en bij voorkeur ook `push` naar `main`).
2. Een job met de **job-naam** `ci` (`jobs.<id>.name: ci`, of job-id `ci` zonder `name`). Die job draait de build/tests/lint van het project.
3. De workflow mag geen `paths:`-filter hebben die de job op sommige PR's overslaat; een overgeslagen workflow rapporteert geen status en blokkeert de PR.
4. Pas de naam in de ruleset (Settings → Rules → Rulesets → `required_status_checks`) aan als je de job anders noemt.

Voorbeeld:

```yaml
name: CI
on:
  pull_request:
jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "voeg hier build/test commando's toe"
```

Heeft een project (nog) geen CI, verwijder dan tijdelijk de regel `required_status_checks` uit de ruleset.
