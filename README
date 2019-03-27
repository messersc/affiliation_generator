# Affiliation generator

Generating a correct list of affiliations for a manuscript can be painful enough,
but editing and amending it can be even worse.

This little python snippet allows you to generate the list of affiliations for you,
if provided with a yaml file that holds the necessary information. See the example.

# Usage

```console
$ cat affiliations.example.yaml
Jane Doe:
  - Institute A, University X
Max Mustermann:
  - Institute B, University Y
  - Research Center

$ python3 generator.py affiliations.example.yaml
Jane Doe 1, Max Mustermann 2,3

1 Institute A, University X
2 Institute B, University Y
3 Research Center
```
