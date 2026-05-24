import subprocess
from pathlib import Path


def run_command(command: list[str]) -> None:
    print(f"\nRunning: {' '.join(command)}")
    subprocess.run(command, check=True)


def main() -> None:
    Path("data").mkdir(exist_ok=True)
    Path("results").mkdir(exist_ok=True)

    run_command([
        "python",
        "scripts/generate_synthetic_dataset.py",
        "--out",
        "data/simulated_clinical.csv",
        "--n",
        "1000",
        "--T",
        "48"
    ])

    run_command([
        "python",
        "scripts/train_pl_primecare.py",
        "--data",
        "data/simulated_clinical.csv",
        "--max_epochs",
        "20"
    ])

    run_command([
        "python",
        "scripts/evaluate_primecare.py"
    ])

    run_command([
        "python",
        "scripts/generate_figures.py"
    ])

    print("\nAll PRIME-Care experiments completed successfully.")


if __name__ == "__main__":
    main()
