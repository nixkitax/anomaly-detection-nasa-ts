from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    base = Path("data/processed/MSL")
    sensor_id = "C-1"

    train = np.load(base / "train" / f"{sensor_id}.npy")
    test = np.load(base / "test" / f"{sensor_id}.npy")
    labels = np.load(base / "labels" / f"{sensor_id}.npy")

    print("Sensor:", sensor_id)
    print("Train shape:", train.shape)
    print("Test shape:", test.shape)
    print("Labels shape:", labels.shape)
    print("Anomaly ratio (test):", float(labels.mean()))

    plt.figure(figsize=(12, 4))
    plt.plot(test, label="", color="blue")
    plt.plot(labels * float(np.max(test)), label="anomaly mask (scaled)", color="magenta", alpha=0.4)
    plt.title(f"MSL {sensor_id}: test signal + anomaly mask")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
