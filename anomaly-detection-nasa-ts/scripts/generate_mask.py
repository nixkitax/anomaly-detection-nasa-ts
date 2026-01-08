import numpy as np # type: ignore 
import pandas as pd # type: ignore
from pathlib import Path


def generate_mask(sensor_id, csv_path, test_path, output_path):
    df = pd.read_csv(csv_path)
    df = df[df["chan_id"] == sensor_id]

    if df.empty:
        raise ValueError(f"Nessuna riga trovata per {sensor_id}")

    test_data = np.load(test_path)
    test_len = test_data.shape[0]

    # Estrai le sequenze di anomalia
    anomaly_sequences = eval(df["anomaly_sequences"].values[0])

    # Costruisci maschera
    mask = np.zeros(test_len, dtype=np.uint8)
    for start, end in anomaly_sequences:
        if 0 <= start < end <= test_len:
            mask[start:end] = 1
        else:
            print(f"Intervallo {start}-{end} fuori dai limiti ({test_len})")

    np.save(output_path, mask)
    print(f"[✓] Salvata mask per {sensor_id} ({np.sum(mask)} anomalie su {test_len})")


if __name__ == "__main__":
    base = Path("data")
    sensor_id = "P-1"
    csv_path = base / "nasa-anomaly-detection-dataset-smap-msl" / "labeled_anomalies.csv"
    test_path = base / "processed" / "MSL" / "test" / f"{sensor_id}.npy"
    output_path = base / "processed" / "MSL" / "labels" / f"{sensor_id}.npy"

    generate_mask(sensor_id, csv_path, test_path, output_path)
