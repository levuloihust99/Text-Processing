from pathlib import Path

path = Path(__file__).parent.parent / "assets/altwpot_sound_permutations.txt"
permutations = []
with path.open(mode="r") as reader:
    for line in reader:
        line = line.strip()
        if line:
            permutations.append(line.split(","))

out = []
for perm in permutations:
    target = ["{:X}".format(ord(ch)) for ch in perm[0]]
    for v in perm[1:]:
        source = ["{:X}".format(ord(ch)) for ch in v]
        out.append("{}\t{}".format(" ".join(source), " ".join(target)))

out_path = path.parent / "normalization_vidiacritics.tsv"
with out_path.open(mode="w") as writer:
    writer.write("\n".join(out) + "\n")