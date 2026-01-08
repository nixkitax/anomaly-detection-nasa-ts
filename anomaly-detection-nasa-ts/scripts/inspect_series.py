from pathlib import Path
import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import pandas as pd # type: ignore

def generate_mask(sensor_id, csv_path, test_path, output_path):
    df = pd.read_csv(csv_path)
    df = df[df["chan_id"] == sensor_id]

    if df.empty:
        raise ValueError(f"Nessuna riga trovata per {sensor_id}")

    test_data = np.load(test_path)
    test_len = test_data.shape[0]

    
    anomaly_sequences = eval(df["anomaly_sequences"].values[0])

    
    mask = np.zeros(test_len, dtype=np.uint8)
    for start, end in anomaly_sequences:
        if 0 <= start < end <= test_len:
            mask[start:end] = 1
        else:
            print(f"Intervallo {start}-{end} fuori dai limiti ({test_len})")

    np.save(output_path, mask)
    print(f"[✓] Salvata mask per {sensor_id} ({np.sum(mask)} anomalie su {test_len})")

def load_or_generate_labels(sensor_id: str, base_dir: Path) -> np.ndarray:
    label_path = base_dir / "labels" / f"{sensor_id}.npy"

    if label_path.is_file():
        labels = np.load(label_path)
    else:
        print(f"[!] Labels not found for {sensor_id}, generating...")
        csv_path = Path("data/nasa-anomaly-detection-dataset-smap-msl/labeled_anomalies.csv")
        test_path = base_dir / "test" / f"{sensor_id}.npy"
        generate_mask(sensor_id, csv_path, test_path, label_path)
        labels = np.load(label_path)

    return labels

def main() -> None:
    base = Path("data/processed/MSL")
    sensor_id = "P-2"


    train = np.load(base / "train" / f"{sensor_id}.npy")
    test = np.load(base / "test" / f"{sensor_id}.npy")
    
    labels = load_or_generate_labels(sensor_id, base)

    print("Sensor:", sensor_id)
    print("Train shape:", train.shape)
    print("Test shape:", test.shape)
    print("Labels shape:", labels.shape)
    print("Anomaly ratio (test):", float(labels.mean()))
    print("Shape:", labels.shape)
    print("Dtype:", labels.dtype)
    print("Min:", labels.min())
    print("Max:", labels.max())
    print("Unique values (rounded):", np.unique(np.round(labels, 2)))

    plt.figure(figsize=(12, 4))

    # Plot only the first signal/dimension
    signal = test[:, 0] if test.ndim == 2 else test

    plt.plot(signal, label="signal", color="blue", linewidth=1)

    # Add shaded regions for anomalies
    anomaly_indices = labels == 1
    plt.fill_between(
        np.arange(len(signal)),
        np.min(signal),
        np.max(signal),
        where=anomaly_indices,
        color="magenta",
        alpha=0.2,
        label="anomaly region"
    )

    plt.title(f"MSL {sensor_id}: test signal + anomaly mask")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
