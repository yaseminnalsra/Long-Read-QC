#!/usr/bin/env python3

import argparse
import gzip
from pathlib import Path
from Bio import SeqIO
import csv


def gc_content(seq: str) -> float:
    if len(seq) == 0:
        return 0.0
    gc = seq.count("G") + seq.count("C") + seq.count("g") + seq.count("c")
    return round(gc / len(seq) * 100, 4)


def mean_quality(scores: list) -> float:
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 4)


def open_fastq(path: str):
    p = Path(path)
    if p.suffix in (".gz", ".gzip"):
        return gzip.open(path, "rt")
    return open(path, "r")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fastq",  required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--sample", default="sample")
    args = parser.parse_args()

    fields = ["sample_id", "read_id", "read_length", "gc_content_pct", "mean_quality"]

    total = 0
    with open_fastq(args.fastq) as fq, open(args.output, "w", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=fields)
        writer.writeheader()

        for rec in SeqIO.parse(fq, "fastq"):
            seq = str(rec.seq)
            writer.writerow({
                "sample_id":      args.sample,
                "read_id":        rec.id,
                "read_length":    len(seq),
                "gc_content_pct": gc_content(seq),
                "mean_quality":   mean_quality(rec.letter_annotations["phred_quality"]),
            })
            total += 1
            if total % 10_000 == 0:
                print(f"  {total:,} read işlendi...", flush=True)

    print(f"Tamamlandı: {total:,} read → {args.output}")


if __name__ == "__main__":
    main()
