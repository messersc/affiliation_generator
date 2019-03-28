import pprint
import sys
import yaml
import yamlordereddictloader

with open(sys.argv[1]) as f:
    yaml_data = yaml.load(f, Loader=yamlordereddictloader.Loader)

affi_dict = dict()
i=1

for author, affils in yaml_data.items():
    for affil in affils:
        if affil not in affi_dict.keys():
            affi_dict[affil] = i
            i += 1

def print_affil_numbers(author):
    affiliations = yaml_data[author]
    affil_numbers = sorted([affi_dict[x] for x in affiliations])
    affil_numbers = [str(x) for x in affil_numbers]
    return (author + " " + ",".join(affil_numbers))

l = [print_affil_numbers(author) for author in yaml_data.keys()]
print(", ".join(l))

print("")

for k,v in affi_dict.items():
    print(" ".join([str(v), k]))

