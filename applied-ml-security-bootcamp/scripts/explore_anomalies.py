from pathlib import Path
import pandas as pd  # type: ignore
import ast

def parse_class_field(value: str) -> list[str]:
    """
    Converte il campo 'class' del CSV in una lista di stringhe.
    Esempi input:
      "[point]" -> ["point"]
      "[contextual, contextual]" -> ["contextual", "contextual"]
    """
    if not isinstance(value, str):
        return []

    value = value.strip()

    # rimuove [ ]
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]

    # split per virgola
    classes = [v.strip() for v in value.split(",") if v.strip()]
    return classes

def parse_list_field(value: str) -> list[list[int]]:
    """
    Converte il campo 'anomaly_sequences' in una lista di liste di interi.
    Esempi input:
      '[[550, 750], [2100, 2210]]' -> [[550, 750], [2100, 2210]]
    """
    import ast

    if not isinstance(value, str):
        return []

    try:
        parsed = ast.literal_eval(value)
        if isinstance(parsed, list):
            return parsed
    except Exception:
        pass

    return []

def main() -> None:
    csv_path = Path(
        "data/nasa-anomaly-detection-dataset-smap-msl/labeled_anomalies.csv"
    )
    df = pd.read_csv(csv_path)

    print("📊 Statistiche generali\n")

    # =========================
    # 1. Canali
    # =========================
    total_channels = len(df)
    msl_channels = (df["spacecraft"] == "MSL").sum()
    smap_channels = (df["spacecraft"] == "SMAP").sum()

    print(f"- Numero totale di canali: {total_channels}")
    print(f"- MSL: {msl_channels} canali")
    print(f"- SMAP: {smap_channels} canali")

    # =========================
    # 2. Conteggio anomalie
    # =========================
    total_anomalies = 0
    point_anomalies = 0
    contextual_anomalies = 0
    channels_with_multiple = 0

    for _, row in df.iterrows():
        anomaly_sequences = parse_list_field(row["anomaly_sequences"])  # converte stringa tipo '[[1, 2]]'
        anomaly_classes = parse_class_field(row["class"])               # converte '[point]' → ["point"]

        if len(anomaly_sequences) > 1:
            channels_with_multiple += 1

        for anomaly_class in anomaly_classes:
            total_anomalies += 1
            if anomaly_class == "point":
                point_anomalies += 1
            elif anomaly_class == "contextual":
                contextual_anomalies += 1
    print(f"- Canali con più di 1 sequenza anomala: {channels_with_multiple}")
    print(f"- Sequenze anomale totali: {total_anomalies}")
    print(f"  - Point anomalies: {point_anomalies}")
    print(f"  - Contextual anomalies: {contextual_anomalies}")

    print(
        f"- Media anomalie per canale: "
        f"{total_anomalies / total_channels:.2f}"
    )


if __name__ == "__main__":
    main()