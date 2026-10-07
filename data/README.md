# Data

Data files are not versioned.

| | |
|---|---|
| Dataset | Arbres publics sur le territoire de la Ville, consolidated file (`arbres-publics.csv`) |
| Source | https://donnees.montreal.ca/dataset/arbres |
| Licence | CC BY, attribution to the City of Montreal |
| Snapshot | 2026-10-07, 335,494 rows, 33 columns, 135,676,040 bytes |
| SHA-256 | `068031590d3e0ea126f49148fddead573541cf69b5cba1eb752ea7801eb3ca00` |
| Local path | `data/raw/montreal_public_trees_2026-10-07.csv` |

The portal refreshes the file about every two weeks, so use the shared snapshot rather than a new download. Check it with `shasum -a 256 <file>` (macOS, Linux) or `Get-FileHash <file>` (Windows).

Known limitations: the file covers 13 boroughs only, and several columns are empty by design for street or non-street trees. `DHP` is the trunk diameter at 1.4 m.
