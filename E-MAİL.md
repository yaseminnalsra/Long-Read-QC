Dear Prof. Dr. KILIÇ,

I performed the quality control analysis of the data from the sample you sent using the Nanoplot tool. As a result of this analysis, you can access visualisations of basic quality metrics such as the read length distribution, Phread quality score distribution, and GC content distribution for your data. 

Findings

A total of 81,001 reads were analysed, with a median read length of 547 bp, an average of 1,038 bp, and an N50 value of 1,761 bp. The distribution is markedly right-skewed, indicating the presence of a large number of short reads; this is likely due to DNA fragmentation during library preparation. However, ultra-long reads reaching 686,155 bp were also detected.
Quality Score: The median Phred score was determined to be Q17.3, with an average of Q17.9; this value corresponds to approximately 98% base call accuracy. Two distinct peaks (around Q7-10 and Q20-25) were observed in the distribution. This bimodal structure can be explained by the coexistence of simplex and duplex reads.
GC Content: The average GC content was 53%, and the distribution exhibited a normal curve. No anomalies indicative of contamination or systematic bias were detected. 

Recommendation

The overall quality of the data is considered to be sufficient. Before proceeding to the alignment stage, it is recommended to filter out low-quality reads (Q < 10) and very short reads (< 200 bp). Alignment can be performed after these filters have been applied. I await your approval for the next step.


Best Regards,
Yasemin
