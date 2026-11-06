# KI-radaren

En interaktiv radar over kritiske spørsmål ved bruk av KI i et statistikkbyrå, med KI-kompasset som overlegg.
Konsept: Thomas Bjørnskau, 2026. Utkast: plassering, ring og pregnans er vurderinger, ikke målinger.

## Innhold

| Fil | Hva |
| --- | --- |
| `index.html` | Hele appen (HTML, CSS og JavaScript i én fil, ingen byggesteg) |
| `tema.json` | Eneste datakilde: temaer, posisjoner per år, kompass, kilder og AI 2027-scenarioet |
| `lag_data.py` | Skriptet som lager `tema.json`. Rediger her, eller rediger JSON-en direkte |

## Publisere på GitHub Pages

1. Legg filene i roten av repoet `ki-radar`.
2. Settings → Pages → Deploy from a branch → `main` / `(root)`.
3. Siden ligger da på `https://<bruker>.github.io/ki-radar/`.

Appen henter `tema.json` med `fetch`, så den må åpnes via en webserver. Lokalt: `python3 -m http.server` og åpne `http://localhost:8000`.

## Funksjoner

- Radar med fire kvadranter: vår egen bruk ↔ vårt samfunnsoppdrag, faglig og epistemisk ↔ makt og rettferdighet.
- Ringer for tidshorisont (nå, 1–3 år, horisont). Størrelse og fyll viser pregnans.
- Tidslinje 2023–2027 med avspilling. 2024 og 2025 er interpolert. 2027 viser scenarioet AI 2027 og er merket som scenario.
- Kompass som overlegg: verdiordene ved polene, med meg/oss-tiltak i panelet.
- Filter på skadetype og nye temaer. Listevisning for oversikt, mobil og skjermleser.
- Mørk modus som standard, lys modus som valg.

## Vurderinger og workshop

- Hver bruker gir egen pregnans og ring per tema. Det lagres bare i nettleseren (localStorage).
- «Lagre og samle» → last ned som JSON (`format: ki-radar-vurdering`).
- Etter en workshop: last inn flere filer → «Samlet» viser gjennomsnitt, og en stiplet ring rundt punktet viser uenighet om tidshorisonten.
- Ingenting sendes til noen server. Filene inneholder bare navn/gruppe, seksjon, vurderinger og notater som brukeren selv skriver.

## Datamodell (kort)

- `temaer[].vinkel`: grader, 0 = øst, mot klokka. Kvadranten avledes av vinkelen.
- `temaer[].posisjon[år]`: `r` (0–1, avstand fra sentrum) og `p` (pregnans 1–3). Mellomliggende år interpoleres.
- `temaer[].type`: `E` faglig, `L` makt, `K` blandet eller kostnad.
- `kvadranter[].kompass`: hvilke to verdiord som svarer på kvadranten.

## Kilder

Se `kilder` i `tema.json`. Temaer uten kilde er egne vurderinger.
