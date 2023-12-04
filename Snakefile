rule prepare:
  shell:
    "python scripts/prepare.py"

rule profile:
  shell:
    "python scripts/profile.py"