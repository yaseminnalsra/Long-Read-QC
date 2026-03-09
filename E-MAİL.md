Dear Professor KILIÇ,

I have completed the quality control analysis of the sequencing data you provided using NanoPlot. Below is a summary of the key findings, along with visualisations of the main quality metrics: read length distribution, Phred quality score distribution, and GC content distribution.

Findings

A total of 81,011 reads were analysed. The median read length was 547 bp, the mean was 1,038 bp, and the N50 value was 1,761 bp. The distribution is markedly right-skewed, suggesting a substantial proportion of short reads — most likely a result of DNA fragmentation during library preparation. Notably, ultra-long reads of up to 686,155 bp were also detected, which is a strength of the long-read sequencing platform used.

Regarding read quality, the median Phred score was Q17.3 and the mean was Q17.9, corresponding to approximately 98% base-calling accuracy. The quality score distribution showed two distinct peaks (around Q7–10 and Q20–25), which is consistent with the coexistence of simplex and duplex reads — a common characteristic of this sequencing technology.

The mean GC content was 53%, and the distribution followed a normal curve. No anomalies suggesting contamination or systematic bias were detected.

Recommendation

The overall data quality is considered sufficient to proceed with downstream analysis. Prior to alignment, I recommend filtering out low-quality reads (Q < 10) and very short reads (< 200 bp) to improve mapping accuracy. Once these filters are applied, alignment to the reference genome can be carried out using a long-read-compatible tool such as minimap2.

Please let me know if you would like to proceed to the alignment step or if you have any questions regarding these results.

Best regards,

Yasemin ARSLAN
