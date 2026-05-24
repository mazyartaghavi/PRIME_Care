install:
	pip install -r requirements.txt

test:
	pytest -q

generate-data:
	python scripts/generate_synthetic_dataset.py --out data/simulated_clinical.csv --n 1000 --T 48

train:
	python scripts/train_pl_primecare.py --data data/simulated_clinical.csv --max_epochs 20

evaluate:
	python scripts/evaluate_primecare.py

figures:
	python scripts/generate_figures.py

run-all: generate-data train evaluate figures
