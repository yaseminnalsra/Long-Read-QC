#!/usr/bin/env python3


import argparse
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

sns.set_theme(style="whitegrid", context="paper", font_scale=1.2)
COLORS = {"gc": "#2E86AB", "length": "#A23B72", "quality": "#F18F01"}
DPI = 150

def stat_lines(ax, s, color):
    ax.axvline(s.mean(),   color=color, ls="--", lw=1.8, label=f"Average = {s.mean():.2f}")
    ax.axvline(s.median(), color=color, ls=":",  lw=1.8, label=f"Median   = {s.median():.2f}")
    ax.legend(fontsize=9)


def n50(lengths: pd.Series) -> float:
    s = lengths.sort_values(ascending=False)
    return float(s[s.cumsum() >= s.sum() / 2].iloc[0])


def plot_gc(df, sample):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df["gc_content_pct"], bins=50, kde=True,
                 color=COLORS["gc"], edgecolor="white", ax=ax)
    stat_lines(ax, df["gc_content_pct"], COLORS["gc"])
    ax.set_xlabel("GC Content (%)")
    ax.set_ylabel("Read Count")
    ax.set_title(f"{sample} — GC Content Distribution", fontweight="bold")
    fig.tight_layout()
    fname = f"{sample}_gc_content.png"
    fig.savefig(fname, dpi=DPI)
    plt.close(fig)
    print(f"[plot] Kaydedildi: {fname}")


def plot_length(df, sample):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    sns.histplot(df["read_length"], bins=80, kde=True,
                 color=COLORS["length"], edgecolor="white", ax=ax1)
    stat_lines(ax1, df["read_length"], COLORS["length"])
    ax1.set_xlabel("Read Length (bp)")
    ax1.set_ylabel("Read Count")
    ax1.set_title("Lineer Scale")

    log_l = np.log10(df["read_length"].clip(lower=1))
    sns.histplot(log_l, bins=80, kde=True,
                 color=COLORS["length"], edgecolor="white", ax=ax2)
    stat_lines(ax2, log_l, COLORS["length"])
    ax2.set_xlabel("Read Length (log₁₀ bp)")
    ax2.set_ylabel("")
    ax2.set_title("Log Scale")

    fig.suptitle(f"{sample} — Read Length Distribution", fontweight="bold")
    fig.tight_layout()
    fname = f"{sample}_read_length.png"
    fig.savefig(fname, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"[plot] Kaydedildi: {fname}")


def plot_quality(df, sample):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df["mean_quality"], bins=50, kde=True,
                 color=COLORS["quality"], edgecolor="white", ax=ax)
    stat_lines(ax, df["mean_quality"], COLORS["quality"])


    for q, ls in [(7, ":"), (10, "--"), (20, "-.")]:
        ax.axvline(q, color="grey", ls=ls, lw=1.1, label=f"Q{q}")
    ax.legend(fontsize=8, ncol=2)

    ax.set_xlabel("Mean Phred Quality Score")
    ax.set_ylabel("Read Count")
    ax.set_title(f"{sample} — Quality Score Distribution", fontweight="bold")
    fig.tight_layout()
    fname = f"{sample}_mean_quality.png"
    fig.savefig(fname, dpi=DPI)
    plt.close(fig)
    print(f"[plot] Saved: {fname}")
# ── summary statistics ───────────────────────────────────────
def summary(df, sample):
    cols = {
        "gc_content_pct": "GC Content (%)",
        "read_length":    "Read Length (bp)",
        "mean_quality":   "Mean Quality",
    }
    rows = []
    print("\n" + "="*55)
    print("  SUMMARY STATISTICS")
    print("="*55)
    for col, label in cols.items():
        s = df[col]
        row = {
            "sample": sample, "metric": label,
            "n": len(s), "mean": round(s.mean(), 3),
            "median": round(s.median(), 3), "std": round(s.std(), 3),
            "min": round(s.min(), 3), "max": round(s.max(), 3),
            "Q25": round(s.quantile(0.25), 3), "Q75": round(s.quantile(0.75), 3),
        }
        if col == "read_length":
            row["N50_bp"] = round(n50(df["read_length"]), 1)
        print(f"\n  ▸ {label}")
        print(f"    Read count  : {int(row['n']):,}")
        print(f"    Mean        : {row['mean']}")
        print(f"    Median      : {row['median']}")
        print(f"    Std         : {row['std']}")
        print(f"    Min / Max   : {row['min']} / {row['max']}")
        print(f"    Q25 / Q75   : {row['Q25']} / {row['Q75']}")
        if "N50_bp" in row:
            print(f"    N50         : {row['N50_bp']} bp")
        rows.append(row)
    print("\n" + "="*55 + "\n")
    out = pd.DataFrame(rows)
    fname = f"{sample}_summary_statistics.csv"
    out.to_csv(fname, index=False)
    print(f"[plot] Summary saved: {fname}")




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",  required=True)
    parser.add_argument("--sample", default="sample")
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    if df.empty:
        sys.exit("HATA: CSV dosyası boş.")

    print(f"[plot] {len(df):,} read yüklendi.")

    plot_gc(df,      args.sample)
    plot_length(df,  args.sample)
    plot_quality(df, args.sample)
    summary(df,      args.sample)


if __name__ == "__main__":
    main()
