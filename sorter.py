from pathlib import Path
import re
import shutil


# sorter.py ligger i rotmappen til prosjektet.
PROSJEKTMAPPE = Path(__file__).resolve().parent
KILDEMAPPE = PROSJEKTMAPPE / "dataset" / "COFACTOR_Res_Dataset3_files"
UTMAPPE = PROSJEKTMAPPE / "dataset" / "sortert"


def trygt_mappenavn(verdi: str) -> str:
    """Gjor en verdi trygg aa bruke som navn paa en mappe."""
    verdi = re.sub(r"\s*,\s*", "_", verdi.strip())
    verdi = re.sub(r"[^\w.-]+", "_", verdi, flags=re.UNICODE)
    return verdi.strip("_.") or "Ukjent"


def les_metadata(fil: Path) -> tuple[str, str]:
    """Les location og building_category fra starten av en TXT-fil."""
    location = None
    kategori = None

    with fil.open("r", encoding="utf-8-sig", errors="replace") as innfil:
        for linjenummer, linje in enumerate(innfil, start=1):
            # Metadataen ligger forst i filen. Ikke les alle maaledataene.
            if linjenummer > 100 or linje.startswith("TimeStamp;"):
                break

            nokkel, skilletegn, verdi = linje.strip().partition(";")
            if not skilletegn:
                continue

            if nokkel.strip().lower() == "location":
                location = verdi.strip()
            elif nokkel.strip().lower() == "building_category":
                kategori = verdi.strip()

    if not location or not kategori:
        raise ValueError("fant ikke location og building_category")

    return trygt_mappenavn(location), trygt_mappenavn(kategori)


def sorter_filer() -> None:
    if not KILDEMAPPE.is_dir():
        raise FileNotFoundError(f"Fant ikke kildemappen: {KILDEMAPPE}")

    txt_filer = sorted(KILDEMAPPE.rglob("*.txt"))
    flyttet = 0
    hoppet_over = 0

    for fil in txt_filer:
        try:
            location, kategori = les_metadata(fil)
        except (OSError, ValueError) as feil:
            print(f"Hopper over {fil.name}: {feil}")
            hoppet_over += 1
            continue

        maalmappe = UTMAPPE / location / kategori
        maalfil = maalmappe / fil.name

        if maalfil.exists():
            print(f"Finnes allerede, hopper over: {maalfil}")
            hoppet_over += 1
            continue

        maalmappe.mkdir(parents=True, exist_ok=True)
        shutil.move(str(fil), str(maalfil))
        print(f"Flyttet {fil.name} -> {location}/{kategori}/")
        flyttet += 1

    print(f"\nFerdig. Flyttet {flyttet} filer. Hoppet over {hoppet_over} filer.")
    print(f"De sorterte filene ligger i: {UTMAPPE}")


if __name__ == "__main__":
    sorter_filer()
