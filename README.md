# Scrum project template

Welkom bij jouw Scrum project repository.

Deze repository is de start voor je projectteam en bevat de basis voor een goede Scrum workflow in GitHub. Je vindt hier de standaard voor user stories, pull requests, review, en projectbeheer.

## Wat staat er al in deze repository?

- een template voor user stories
- een pull request template
- een checklist voor Definition of Ready
- een checklist voor Definition of Done
- een handleiding voor de GitHub Project setup
- automatische checks voor de projectstatus

## Hoe werk je met deze repo?

1. Maak een issue aan met een user story.
2. Controleer of de story voldoet aan de Definition of Ready.
3. Zet de story in de backlog of in de sprint.
4. Wijs één persoon aan als eigenaar van de story.
5. Gebruik de gekoppelde branch voor de ontwikkeling.
6. Open een pull request wanneer de story klaar is.
7. Vraag om review en controleer de acceptatiecriteria.
8. Merge pas nadat alles is goedgekeurd.

## Definition of Ready

Een story mag pas naar de backlog als deze voldoet aan de Definition of Ready.

Lees hier:
- `docs/definition-of-ready.md`

## Definition of Done

Een story is pas Done als alle acceptatiecriteria zijn gehaald, de tests zijn uitgevoerd en de pull request is goedgekeurd en gemerged.

Lees hier:
- `docs/definition-of-done.md`

## GitHub Project

Jouw team werkt met een GitHub Project voor planning, status, prioriteit en sprintinzicht.

Lees hier:
- `docs/github-project-setup.md`

## Branch protection en review

De `main` branch wordt beschermd tegen onveilige merges. Denk aan:

- pull request verplicht
- minimaal één review
- reviewcommentaar moet opgelost zijn
- geen directe merge zonder goedkeuring

## Werkwijze per sprint

- check de backlog
- kies de stories voor de sprint
- wijs een eigenaar toe
- werk in de gekoppelde branch
- open een PR
- review en merge
- update de status in het project

## Nieuwe team setup

Voor een nieuw team is er een korte handleiding beschikbaar met alle stappen die je moet doen om een nieuwe repo en project op te zetten.

Lees hier:
- `docs/new-team-setup.md`

## Belangrijk

Gebruik altijd één duidelijke user story per issue.  
Maak een story klein genoeg om in één sprint af te ronden.  
Schrijf acceptatiecriteria en testplan zodat de story controleerbaar is.

## Structuur van deze repo

- `.github/ISSUE_TEMPLATE/` – templates voor issues
- `.github/workflows/` – automatische checks en workflows
- `.github/scripts/` – scripts voor projectcontrole
- `docs/` – handleidingen en afspraken