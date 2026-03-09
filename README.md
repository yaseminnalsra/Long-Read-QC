Long Read Quality Control Pipeline

A Nextflow pipeline for quality control of Oxford Nanopore long-read sequencing data. It runs NanoPlot, computes per-read statistics, and generates distribution plots for GC content, read length, and quality scores.

---

## Requirements

- N E X T F L O W   ~  version 25.10.4  
- Docker  
- Python 3.12.3 with required packages (installed inside the container):

  - Biopython
  - NanoPlot
  - pandas
  - numpy
  - matplotlib
  - seaborn

---

## Directory Structure
```
longread_QC/
├── raw/
│   └── ***.fastq           
├── scripts/
│   ├── read_stats.py        # Per-read statistics calculation
│   └── plot_stats.py        # Distribution plot generation
├── results
├── main.nf                  # Nextflow pipeline (DSL2)
├── nextflow.config          # Configuration 
├── samplesheet.csv          # Input sample list
└── Dockerfile
```

---

## Sample Sheet Example (csv)
```
sample,fastq
SAMPLE1_SE,/your/path/sample1.fastq
SAMPLE2_SE,/your/path/sample2.fastq
```
## If your sample are pair-end
```
sample,fastq_1,fastq_2
SAMPLE1_PE,/your/path/sample1_1.fastq,/your/path/sample1_2.fastq
SAMPLE2_PE,/your/path/sample2_1.fastq,/your/path/sample2_2.fastq
```
---
## Usage

Build the Docker image:
```
docker build -t longread_qc:latest .
```
Run the pipeline:
```
nextflow run main.nf -with-docker
```
All outputs will be collected in the results/ folder:

*_nanoplot/ → NanoPlot QC reports

*_stats.csv → Read-level statistics

*_stats_plots/ → Histogram and distribution plots

## Example Output

### Read Length Distribution
![Read Length](results/SAMPLE1_SE_plots/SAMPLE1_SE_read_length.png)
### Quality Distribution
![Quality](results/SAMPLE1_SE_plots/SAMPLE1_SE_mean_quality.png)
### GC Content Distribution
![GC Content](results/SAMPLE1_SE_plots/SAMPLE1_SE_gc_content.png)
