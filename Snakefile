rule prepare:
  shell:
    "python scripts/prepare_data.py"

rule profile:
  shell:
    "python scripts/profile.py"