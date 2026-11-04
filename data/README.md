# Data

The raw file is not stored in Git. The processed file of Deliverable 2 is (see [Processed file](#processed-file)).

| | |
|---|---|
| Name | Arbres publics sur le territoire de la Ville (consolidated file) |
| Owner | City of Montreal, Service des grands parcs, du verdissement et du Mont-Royal |
| Original source | https://donnees.montreal.ca/dataset/arbres |
| Copy used | https://doi.org/10.5281/zenodo.23540888 |
| Licence | CC BY 4.0 (http://creativecommons.org/licenses/by/4.0/) |
| Snapshot | 2026-10-07 |
| Size | 335,494 rows, 33 columns, 135,676,040 bytes |
| SHA-256 | `068031590d3e0ea126f49148fddead573541cf69b5cba1eb752ea7801eb3ca00` |
| MD5 | `23c6f9a7b5b72a24e05e266972c76856` (same as the portal record of 2026-10-07) |
| Local path | `data/raw/montreal_public_trees_2026-10-07.csv` |

The portal replaces the file every day and keeps no old versions. The Zenodo record is an unchanged copy of the snapshot. The whole project uses this copy only, never a newer download.

## Getting the file

The D2 notebook downloads it from Zenodo when it is missing, then checks the SHA-256 and stops if it differs.

To do it by hand, save the file of the Zenodo record at the local path above and check it:

```bash
shasum -a 256 data/raw/montreal_public_trees_2026-10-07.csv
```

On Windows, use `Get-FileHash <file>` in PowerShell.

## Processed file

`data/processed/trees_encoded.csv` is the output of the Deliverable 2 notebook (the `to_csv` line of section 3): cleaned and encoded, not scaled. Later deliverables read it instead of cleaning the raw file again.

| | |
|---|---|
| Content | 334,950 rows, 62 columns (61 features and `DHP`), the first column `raw_row` is the row number in the raw file |
| Size | 51,012,408 bytes |
| SHA-256 | `a07265322bbe351c7abf45a8c404188bd015d481cb20412580eca3713bc3b477` |

If the cleaning of Deliverable 2 changes, create the file again and commit it.

## Citation

Ville de Montréal, Service des grands parcs, du verdissement et du Mont-Royal (2026). *Arbres publics sur le territoire de la Ville (consolidated file), snapshot of 2026-10-07* (Version 2026-10-07) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.23540888

## Known limitations

- The file covers 13 boroughs only.
- Several columns are empty by design for street or non-street trees.
- `DHP` is the trunk diameter at 1.4 m. The unit is not given in the data dictionary.
