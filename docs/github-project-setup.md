# GitHub Project-instellingen

Maak vanuit het organisatieproject een kopie per team. Koppel daarna precies één teamrepository aan die kopie.

## Velden

Issuetype `User Story` en de issuevelden `Priority` en `Points` worden op organisatieniveau beheerd (Organization settings → Planning). Voeg ze in het project als kolom toe.

| Naam | Type | Waarden / afspraak |
| --- | --- | --- |
| Status | Single select | `Draft`, `Backlog`, `Sprint (To do)`, `In progress`, `In review`, `Done` |
| Sprint | Iteration | Standaard één week. Pas de duur van alleen de betreffende iteratie aan als een sprint twee weken duurt. |
| Priority | Org-issueveld (single select) | `Must have`, `Should have`, `Could have`, `Won't have` |
| Points | Org-issueveld (number) | Story points zonder ureninschatting |
| Milestone | Built-in | Optionele epic |
| Assignees | Built-in | Eén eigenaar zodra de story aan een sprint wordt toegevoegd |

## Views

1. Drafts / refinement — table, filter `Status: Draft`.
2. Backlog — table, filter `Status: Backlog`; sorteer eerst op Priority en groepeer eventueel op Milestone.
3. Current sprint — board, filter `sprint:@current`; groepeer op Status en gebruik Assignees als swimlane.
4. Next sprint — table, filter `sprint:@next`.
5. Roadmap — roadmap, gebruik Sprint als datum en groepeer op Milestone.

Gebruik geen losse view per sprint: `@current` en `@next` veranderen automatisch wanneer een sprint wisselt.

## Workflows

Projectworkflows worden niet meegekopieerd en staan na het kopiëren uit. Schakel in het project de volgende ingebouwde workflows in:

- Auto-add to project: selecteer de teamrepository en gebruik filter `is:issue`; zet nieuwe items op Backlog.
- Item closed → Done (verplicht; anders blijft een gesloten story in een oude status staan).
- Pull request merged → Done.
- Item reopened → In progress.
- Auto-archive: archiveer Done-items na de afgesproken periode, bijvoorbeeld 14 dagen.

## Merge-controle `story-status`

De workflow `story-status.yml` blokkeert (via de ruleset) een pull request tenzij de gekoppelde story:

- via `Closes #nummer` precies één story is,
- issuetype `User Story` heeft en precies één assignee,
- in het project de status `In progress` of `In review` heeft.

Zet de status dus eerst handmatig goed en start de check daarna opnieuw (Re-run in het tabblad Checks): een statuswijziging in het project start geen workflow. Dependabot- en fork-PR's hebben geen toegang tot `PROJECT_TOKEN` en kunnen de check niet doorstaan; een beheerder kan die omzeilen.

## Actions-configuratie

De workflow `check-project.yml` controleert dagelijks of backlog- en sprintstories compleet zijn.

1. Maak in de teamrepo een Actions-secret `PROJECT_TOKEN`. Gebruik een fine-grained personal access token van een beheerder met toegang tot de organisatie en Projects: read. Het token moet ook de gekoppelde repository kunnen lezen en issues kunnen bewerken.
2. Het projectnummer is niet nodig: de checker gebruikt het project dat aan de repository is gekoppeld (precies één open project). Alleen als er meerdere projecten gekoppeld zijn kun je een repository variable `PROJECT_NUMBER` zetten.
3. Als de statusnamen in het project afwijken, pas de omgevingsvariabelen bovenaan `.github/workflows/check-project.yml` aan.

De checker voegt labels toe in plaats van stories automatisch te verplaatsen: `needs-refinement` voor onvolledige Backlog-stories en `needs-sprint-attention` voor stories zonder eigenaar of na een verstreken sprint. Het team beslist vervolgens zelf hoe de story wordt aangepast.
