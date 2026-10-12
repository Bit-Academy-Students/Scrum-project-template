# Scrum project template

Gebruik deze repository als startpunt voor een Scrum-project. Elke GitHub Issue is altijd één user story. Technische taken worden beschreven in de story, de pull request of in een checklist; maak daarvoor geen aparte issues.

## Werkwijze

1. Verzamel nieuwe ideeën als drafts in GitHub Projects.
2. Werk een draft tijdens refinement uit tot een Issue via New issue → User story.
3. Controleer de [Definition of Ready](docs/definition-of-ready.md), zet vervolgens Priority en Points in het project en verplaats de story naar Backlog.
4. Kies tijdens sprint planning stories die in één sprint passen. Vul de Iteration in en wijs precies één eigenaar toe.
5. Zodra een story wordt toegewezen, maakt de workflow een gekoppelde branch. Werk uitsluitend op die branch.
6. Open een pull request naar `main`, laat een ander teamlid reviewen en voldoe aan de [Definition of Done](docs/definition-of-done.md).
7. Merge pas na minimaal één goedkeuring. Gebruik `Closes #nummer` in de PR-beschrijving zodat de story sluit bij merge.

## Projectvelden en views

Maak voor ieder team een kopie van het organisatieproject en richt het in volgens de begeleiding in [GitHub Project-instellingen](docs/github-project-setup.md).

| Veld | Type | Gebruik |
| --- | --- | --- |
| Status | Single select | Draft, Backlog, Sprint (To do), In progress, In review, Done |
| Iteration | Iteration | Standaard één week; pas een afzonderlijke iteratie aan naar twee weken wanneer nodig |
| Priority | Single select | Must have, Should have, Could have, Won't have |
| Points | Number | Story points; gebruik geen uren naast points |
| Milestone | Built-in | Optionele epic |
| Assignees | Built-in | Exact één eigenaar wanneer een story de sprint in gaat |

## Teamrepo inrichten

1. Kies Use this template en maak een publieke repository voor het team in `Bit-Academy-Students`.
2. Voeg teamleden toe met schrijfrechten.
3. Kopieer het organisatieproject vanuit Projects → Templates en link de nieuwe repo in de projectinstellingen.
4. Configureer Auto-add met filter `is:issue` voor deze repo. Nieuwe issues komen in Backlog.
5. Voeg de Actions-secret `PROJECT_TOKEN` toe en de repository variable `PROJECT_NUMBER`; zie [GitHub Project-instellingen](docs/github-project-setup.md).
6. Configureer een ruleset voor `main` volgens [Bescherm main](docs/main-branch-ruleset.md).
7. Stel de eerste sprintdatum in; de standaardduur is één week.

## Belangrijkste bestanden

- [Definition of Ready](docs/definition-of-ready.md)
- [Definition of Done](docs/definition-of-done.md)
- [GitHub Project-instellingen](docs/github-project-setup.md)
- [Beschermde main-branch](docs/main-branch-ruleset.md)
