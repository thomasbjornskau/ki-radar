"""Lager tema.json – felles datakilde for appen, figurene og filmen."""
import json

R = 362.0  # radius i figurene; alt lagres normalisert 0–1

KILDER = {
    "imf": {"tittel": "IMF (2026): StatGPT – AI for Official Statistics",
            "url": "https://www.imf.org/en/publications/departmental-papers-policy-papers/issues/2026/03/10/statgpt-ai-for-official-statistics-573514"},
    "iasr": {"tittel": "International AI Safety Report 2026",
             "url": "https://internationalaisafetyreport.org/publication/2026-report-extended-summary-policymakers"},
    "westwood": {"tittel": "Westwood (PNAS 2025), omtalt av Dartmouth",
                 "url": "https://fas.dartmouth.edu/news/2026/04/sean-westwood-wins-pnas-prize-ai-polling-study"},
    "stanford": {"tittel": "Stanford Digital Economy Lab: Canaries in the Coal Mine",
                 "url": "https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/"},
    "iea": {"tittel": "IEA: Energy and AI (omtalt i Scientific American)",
            "url": "https://scientificamerican.com/article/ai-will-drive-doubling-of-data-center-energy-demand-by-2030"},
    "metr": {"tittel": "METR (2025): erfarne utviklere og KI-verktøy",
             "url": "https://arxiv.org/abs/2507.09089"},
    "hlgmos": {"tittel": "UNECE HLG-MOS om generativ KI i statistikkbyråer",
               "url": "https://unstats.un.org/bigdata/events/2025/ai-data-science/webinar2/presentations/Vytas%20and%20Olivier%20-%20%20HLG-MOS%20on%20Generative%20AI%20_UNSD.pdf"},
    "ai2027": {"tittel": "AI 2027 (scenario)", "url": "https://ai-2027.com/"},
}

# id, navn, vinkel, r2026, type, pregnans2026, ny, r2023, p2023, r2027 (scenario), kort, ssb, kilde
T = [
    ("sannhet", "Sannhet i egen bruk", 66, 165, "E", 3, False, 160, 3, None,
     "Språkmodeller lager feil som ser riktige ut, også tall.",
     "Plausible feil er farligere enn åpenbare. Kildekrav og kontroll må bli rutine.", "imf"),
    ("svartboks", "Svart boks", 85, 182, "E", 2, False, 175, 2, None,
     "Vi kan sjelden forklare hvorfor modellen svarte som den gjorde.",
     "Metodedokumentasjon og reproduserbarhet er krav i offisiell statistikk.", "hlgmos"),
    ("glatthet", "Glatthet", 14, 118, "E", 1, False, 150, 1, None,
     "KI-tekst blir generisk, glatt og lik.",
     "Formidlingen kan miste presisjon og særpreg.", None),
    ("avlaering", "Avlæring", 26, 255, "E", 3, False, 320, 2, None,
     "Kompetanse forvitrer når maskinen gjør jobben, og vi stoler for mye på den.",
     "Fagfolk må fortsatt kunne vurdere tallene selv. Leger fant færre svulster etter en periode med KI-støtte.", "iasr"),
    ("hype", "Hype og feil problem", 88, 100, "K", 2, False, 100, 2, None,
     "KI tas i bruk fordi det er mulig, ikke fordi det løser riktig problem.",
     "Opplevd og faktisk effekt kan sprike: erfarne utviklere ble tregere, men trodde de ble raskere.", "metr"),
    ("konf", "Konfidensialitet og personvern", 140, 122, "L", 3, False, 150, 3, None,
     "Data sendes til tjenester vi ikke kontrollerer, og modeller kan huske og lekke.",
     "Statistisk konfidensialitet er eksistensielt for SSB.", "hlgmos"),
    ("ansvar", "Ansvar og agenter", 104, 245, "L", 3, False, 335, 2, 170,
     "Agenter handler selv, og feil kan forplante seg mellom dem.",
     "Hvem eier et tall en agent har laget?", "iasr"),
    ("skjevhet", "Skjevhet i klassifisering", 150, 250, "L", 2, False, 250, 2, None,
     "Modeller som klassifiserer, kan gi systematisk skjeve resultater for grupper.",
     "Gjelder automatisk koding av yrke, næring og fritekst.", None),
    ("sikkerhet", "Sikkerhet og angrep", 172, 262, "L", 2, False, 300, 2, 200,
     "Promptinjeksjon, angrep og misbruk av agenter.",
     "Nye angrepsflater når KI får tilgang til systemer og data.", "iasr"),
    ("leverandor", "Leverandøravhengighet", 177, 132, "L", 3, False, 230, 2, None,
     "Innlåsing hos få leverandører og utenlandsk jurisdiksjon.",
     "Ligger på grensen mellom egen bruk og samfunnsoppdraget.", "hlgmos"),
    ("legitimitet", "Legitimitet og åpenhet", 206, 150, "L", 3, False, 240, 2, None,
     "Allmennhetens tillit og demokratisk forankring.",
     "Tilliten til tallene er oppdraget. Åpenhet om KI-bruk er en del av den.", "hlgmos"),
    ("arbeidsliv", "Arbeidsliv og rekruttering", 226, 248, "L", 2, True, 335, 1, None,
     "KI påvirker arbeidsmarkedet først for de yngste.",
     "Noe SSB må måle, og noe som rammer SSBs egen rekruttering.", "stanford"),
    ("klima", "Klima og ressurser", 250, 122, "K", 2, False, 245, 1, None,
     "Strømforbruket i datasentre ventes å mer enn dobles til 2030.",
     "En tredje type skade: materiell kostnad for samfunnet.", "iea"),
    ("makt", "Maktkonsentrasjon og kappløp", 198, 325, "L", 1, True, 335, 1, 260,
     "Få selskaper og stater kontrollerer de mest avanserte systemene.",
     "Påvirker hvilke verktøy SSB kan velge, og på hvilke vilkår.", "ai2027"),
    ("kontroll", "Tap av kontroll", 238, 335, "L", 1, True, 345, 1, 280,
     "Systemer som utvikler seg raskere enn menneskelig tilsyn.",
     "Lav vekt i dag, men verdt å følge med på.", "ai2027"),
    ("mellomledd", "KI som mellomledd", 278, 150, "E", 3, True, 330, 1, None,
     "Brukere får SSB-tall via chatboter som gjengir dem feil.",
     "Feilene ser troverdige ut og presenteres som om de kom fra SSB.", "imf"),
    ("robot", "Robotsvar i undersøkelser", 324, 170, "E", 3, True, 340, 1, None,
     "KI-respondenter slipper gjennom robotkontroller i nettundersøkelser.",
     "Datagrunnlaget for undersøkelser kan forurenses billig og usynlig.", "westwood"),
    ("maal", "Måleblindsone", 346, 128, "E", 2, True, 230, 1, None,
     "Klarer vi å måle hva KI gjør med arbeidsliv, produktivitet og samfunn?",
     "Et krav til SSB selv, ikke bare en kritikk av KI.", None),
    ("forurenset", "Forurenset informasjonsrom", 302, 252, "E", 2, True, 330, 1, None,
     "Syntetisk innhold og falske «offisielle» tall i informasjonsrommet.",
     "Feilinformasjon kan bli tilskrevet SSB.", "hlgmos"),
]

SCENARIO = [
    ("koder", "Supermenneskelig koder", "mars 2027", 40, "KI-systemer som koder bedre enn de beste menneskene."),
    ("uker", "År med framgang på uker", "2027", 68, "KI som forsker på KI og akselererer utviklingen."),
    ("vekter", "Modellvekter stjålet", "feb 2027", 218, "En stat stjeler vektene til den mest avanserte modellen."),
    ("tilsyn", "Agenter overvåker agenter", "2027", 140, "Mennesker henger etter, svakere KI overvåker sterkere."),
    ("kapplop", "Kappløp USA–Kina", "2027", 250, "Konkurranse presser fram fart på bekostning av sikkerhet."),
    ("agent4", "Agent-4 ser lojal ut", "sep 2027", 316, "En modell som består prøvene, men kan ha andre mål."),
    ("valg", "Bremse eller kappløpe", "okt 2027", 292, "En komité må velge. Scenarioet har to slutter."),
]

def n(v): return round(v / R, 3)

data = {
    "meta": {
        "tittel": "KI-radaren",
        "konsept": "Thomas Bjørnskau, 2026",
        "versjon": "0.1",
        "oppdatert": "2026-11-06",
        "status": "Utkast. Plassering, ring og pregnans er vurderinger, ikke målinger.",
    },
    "ar": [2023, 2024, 2025, 2026, 2027],
    "scenarioAr": 2027,
    "ringer": [
        {"id": "na", "navn": "Nå", "inner": n(58), "ytre": n(192), "midt": n(150)},
        {"id": "snart", "navn": "1–3 år", "inner": n(192), "ytre": n(280), "midt": n(240)},
        {"id": "horisont", "navn": "Horisont", "inner": n(280), "ytre": 1.0, "midt": n(325)},
    ],
    "akser": {
        "nord": {"navn": "Vår egen bruk", "under": "SSB som KI-bruker"},
        "sor": {"navn": "Vårt samfunnsoppdrag", "under": "SSB som kilde, måler og tillitsinstitusjon"},
        "ost": {"navn": "Faglig og epistemisk", "under": "sannhet, kompetanse, dømmekraft"},
        "vest": {"navn": "Makt og rettferdighet", "under": "ansvar, skjevhet, avhengighet, kontroll"},
    },
    "kvadranter": [
        {"id": "no", "navn": "Kvalitet i arbeidet", "kompass": ["etterprovbarhet", "eierskap"]},
        {"id": "nv", "navn": "Ansvar og kontroll", "kompass": ["etterprovbarhet", "kontroll"]},
        {"id": "sv", "navn": "Makt og legitimitet", "kompass": ["forsvarlighet", "kontroll"]},
        {"id": "so", "navn": "Datagrunnlag og formidling", "kompass": ["forsvarlighet", "eierskap"]},
    ],
    "typer": {"E": "Faglig", "L": "Makt", "K": "Blandet eller kostnad"},
    "kompass": [
        {"id": "etterprovbarhet", "navn": "Etterprøvbarhet", "retning": "nord",
         "meg": "La aldri et svar passere uten å sjekke det mot kilde eller egen kunnskap.",
         "oss": "Bygg kildekrav og sporbarhet inn i rutinene, så kontroll blir det normale."},
        {"id": "eierskap", "navn": "Faglig eierskap", "retning": "ost",
         "meg": "Behold eierskap til problemet. La KI utfordre, ikke avgjøre.",
         "oss": "Organiser arbeidet så folk fortsatt gjør fag, ikke bare godkjenner maskiners utkast."},
        {"id": "forsvarlighet", "navn": "Forsvarlighet", "retning": "sor",
         "meg": "Bruk verktøyet der det gir reell verdi, og vær ærlig om at det blir brukt.",
         "oss": "Avvei kostnad mot nytte, og vær åpen om hvor og hvordan KI brukes.",
         "forslag": "Sikre at tallene når fram riktig: ekte respondenter, siterbare og maskinlesbare tall."},
        {"id": "kontroll", "navn": "Kontroll", "retning": "vest",
         "meg": "Kjenn grensene og varsle når noe er på vei utenfor dem.",
         "oss": "Eie databehandling, ansvarslinjer, sikkerhet og leverandørstrategi."},
    ],
    "kilder": KILDER,
    "temaer": [],
    "scenario": [],
}

for (tid, navn, ang, r26, typ, p26, ny, r23, p23, r27, kort, ssb, kilde) in T:
    data["temaer"].append({
        "id": tid, "navn": navn, "vinkel": ang, "type": typ, "ny": ny,
        "kort": kort, "ssb": ssb, "kilde": kilde,
        "posisjon": {"2023": {"r": n(r23), "p": p23}, "2026": {"r": n(r26), "p": p26},
                     "2027": {"r": n(r27 if r27 else r26), "p": p26}},
    })
for (sid, navn, dato, ang, kort) in SCENARIO:
    data["scenario"].append({"id": sid, "navn": navn, "dato": dato, "vinkel": ang, "kort": kort, "kilde": "ai2027"})

json.dump(data, open("tema.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok", len(data["temaer"]), "temaer,", len(data["scenario"]), "scenariopunkter")
