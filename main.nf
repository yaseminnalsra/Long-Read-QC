#!/usr/bin/env nextflow

params.samplesheet = "samplesheet.csv"

Channel
    .fromPath(params.samplesheet)
    .splitCsv(header:true, sep:',')
    .map { row -> tuple(row.sample, file(row.fastq)) }
    .set { reads_ch }

process NANOPLOT {
    tag "$sample"
    input:
    tuple val(sample), path(reads)
    output:
    path "${sample}_nanoplot"
    script:
    """
    NanoPlot --fastq $reads --outdir ${sample}_nanoplot
    """
}

process READ_STATS {
    tag "$sample"
    input:
    tuple val(sample), path(fq)
    output:
    tuple val(sample), path("${sample}_stats.csv")
    script:
    """
    python3 /home/yasemin/longread_QC/scripts/read_stats.py --fastq $fq --output ${sample}_stats.csv --sample $sample
    """
}

process PLOT_STATS {
    tag "$sample"
    publishDir "results/${sample}_plots", mode: 'copy'
    input:
    tuple val(sample), path(stats_csv)
    output:
    tuple val(sample), path("${sample}_gc_content.png"),
                       path("${sample}_read_length.png"),
                       path("${sample}_mean_quality.png"),
                       path("${sample}_summary_statistics.csv")
    script:
    """
    python3 /home/yasemin/longread_QC/scripts/plot_stats.py --input $stats_csv --sample $sample
    """
}

workflow {
    NANOPLOT(reads_ch)
    READ_STATS(reads_ch) | PLOT_STATS
}
