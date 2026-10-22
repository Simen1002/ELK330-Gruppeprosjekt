from pathlib import Path
import pandas as pd


def txt_til_csv(txt_fil, csv_fil):
    csv_fil.parent.mkdir(parents=True, exist_ok=True)

    # Finn raden der datatabellen begynner
    with txt_fil.open("r", encoding="utf-8-sig") as fil:
        for radnummer, linje in enumerate(fil):
            if linje.startswith("TimeStamp;"):
                header_rad = radnummer
                break
        else:
            raise ValueError("Fant ikke TimeStamp-kolonnen")

    data = pd.read_csv(
        txt_fil,
        sep=";",
        skiprows=header_rad,
        usecols=["TimeStamp", "SolGlob", "ElImp"],
    )

    data = data.rename(
        columns={
            "TimeStamp": "tid",
            "SolGlob": "innstraling_W_m2",
            "ElImp": "forbruk_Wh",
        }
    )

    data["tid"] = pd.to_datetime(
        data["tid"],
        format="%Y-%m-%dT%H:%M:%S%z",
        errors="raise",
    )

    tallkolonner = ["innstraling_W_m2", "forbruk_Wh"]

    for kolonne in tallkolonner:
        data[kolonne] = pd.to_numeric(data[kolonne], errors="coerce")

    # Gjør alle negative måleverdier om til 0
    data[tallkolonner] = data[tallkolonner].clip(lower=0)

    data = data.set_index("tid").sort_index()
    data.to_csv(csv_fil, encoding="utf-8")

    print(f"Laget: {csv_fil}")


kildemappe = Path(
    "/Users/simenbakken/repos/Gruppeprosjekt/dataset/sortert"
)

maalmappe = Path(
    "/Users/simenbakken/repos/Gruppeprosjekt/dataset/csv_filer"
)

for txt_fil in kildemappe.rglob("*.txt"):
    relativ_sti = txt_fil.relative_to(kildemappe)
    csv_fil = (maalmappe / relativ_sti).with_suffix(".csv")

    try:
        txt_til_csv(txt_fil, csv_fil)
    except Exception as feil:
        print(f"Feil i {txt_fil}: {feil}")