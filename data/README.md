# Data

Data files are not stored in Git.

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

## Citation

Ville de Montréal, Service des grands parcs, du verdissement et du Mont-Royal (2026). *Arbres publics sur le territoire de la Ville (consolidated file), snapshot of 2026-10-07* (Version 2026-10-07) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.23540888

## Known limitations

- The file covers 13 boroughs only.
- Several columns are empty by design for street or non-street trees.
- `DHP` is the trunk diameter at 1.4 m. The unit is not given in the data dictionary.
