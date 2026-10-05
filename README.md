# Dimer Interaction Energy

Counterpoise-corrected pair interaction.

Required inputs/backend: Two positioned closed-shell fragments; Psi4.

## Files

- `dimer_interaction_energy.py`: calculation/screening code.
- `run.py`: portable Python launcher; `run.bat` for Windows and `run.sh` for Linux/macOS.
- `requirements.txt`: Python packages for this workflow.
- Other `.py` files: supporting code copied into this folder so it can be used independently.
- `examples/`: sample input formats; synthetic numerical data are demonstrations only.

## Install and run

Use Python 3.11/3.12. Open a terminal in this folder.

```bash
python -m venv .venv
```

Windows activation: `.venv\Scripts\activate`. Linux/macOS: `source .venv/bin/activate`.

```bash
python -m pip install -r requirements.txt
python run.py --help
python run.py fragment_A.xyz fragment_B.xyz --out results
```

You can also use `run.bat` or `bash run.sh` with the same arguments.
Input paths are relative to the current terminal directory. Results go to `--out`.

## Scientific scope

Install Psi4. Supply two fragments positioned in their shared dimer geometry; no fabricated dimer coordinates are bundled.

Example numerical energies, shieldings, reference constants and thermodynamic data
are synthetic. The sample XYZ is an MMFF conformer and the sample CIF is a generated
unrelaxed candidate. Neither is an experimentally validated structure. Pseudopotential
filenames are placeholders and must be replaced with real files. Required real inputs
and electronic-structure programs are not bundled. Do not treat screening results as
validated formation probabilities.

See the root VALIDATION.md for completed checks and quantum-engine testing limits.
