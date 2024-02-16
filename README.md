# Validation Template
Template repository for validating relationships and graph view generation

1. Update `validation-config.yml` to add relationships and information about your tables.

```yaml
relationships:
  sub_class_of: rdfs:subClassOf
  part_of: BFO:0000050
  connected_to: RO:0001025

data:
  - name: Kidney
    version: v1.4
    sheet_id: 19B_iDwpVTzLl6JLUl7g943p8b14YxYRwOshm-PLbIwk
    gid: 949267305
  - name: Eye
    version: v1.4_DRAFT
    sheet_id: 1tNNPZXL0ycw5gNksDUKHZJpRkKgRdVAUh9AZ6ohpgOA
    gid: 695483621
  - name: 3D-Reference-Organ
    version: v1.1
    filename: tests/ref-organ-relations.tsv
```

- The output files will be in the folder `output`. Each subfolder will have the outputs for each data defined in the `validation-config.yml`. For example, `output/Kidney`, `output/Eye`, etc.
- The `png` file is the graph view of the table showing the valid and that are not matched relationships.
- The `tsv` file contains the pairs that are not valid according to the source ontologies.
- The output files names will be generated using `{data.name}-{data.version}.{png,tsv}`.

There are two possible ways to pass information about your tables.
- For ASCT+B tables, you need to pass the `sheet_id` and the `gid`
- For general tables, you need to pass the `filename` which is the path to a TSV table with the following columns:

| s                   | slabel                                | user_slabel                               | o                  | olabel                                | user_olabel                               |
|---------------------|---------------------------------------|-------------------------------------------|--------------------|---------------------------------------|-------------------------------------------|
| the subject term ID | the label of the term in the column s | optional label for the term given by user | the object term ID | the label of the term in the column s | optional label for the term given by user |

2. Use Docker as a toolbox to generate the outputs.

- Run the command: `sh run.sh make reports`