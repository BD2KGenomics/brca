releaseDir = $(BRCA_PIPELINE_DATA)
pseudonymDir = $(releaseDir)/pseudonym_generation
inputVcfDir = $(releaseDir)/pipeline_input
inputVcfs = $(inputVcfDir)/10k_genome.brca.sorted.hg38.vcf \
	$(inputVcfDir)/ClinVarBrca.vcf \
	$(inputVcfDir)/sharedLOVD_brca12.sorted.hg38.vcf \
	$(inputVcfDir)/exLOVD_brca12.sorted.hg38.vcf \
	$(inputVcfDir)/bic_brca12.sorted.hg38.vcf \
	$(inputVcfDir)/exac_BRCA12.sorted.hg38.vcf \
	$(inputVcfDir)/esp.brca.vcf


all:	$(releaseDir)/aggregated.tsv

$(releaseDir)/aggregated.tsv:	$(releaseDir)/merged.withVEP.csv aggregate_across_columns.py brca_pseudonym_generator.py
	aggregate_across_columns.py -i $< -o $(releaseDir)/tmp.tsv
	brca_pseudonym_generator.py -i $(releaseDir)/tmp.tsv \
	  -j $(pseudonymDir)/hg18.fa \
	  -k $(pseudonymDir)/hg19.fa -l $(pseudonymDir)/hg38.fa \
	  -r $(pseudonymDir)/refseq_annotation.hg18.gp \
	  -s $(pseudonymDir)/refseq_annotation.hg19.gp \
	  -t $(pseudonymDir)/refseq_annotation.hg38.gp \
	  -o $@

$(releaseDir)/merged.withVEP.csv:	$(releaseDir)/merged.csv add_VEP_result.py
	add_VEP_result.py -i $< -o $@

$(releaseDir)/merged.csv:	$(inputVcfs) variant-merging.py
	variant-merging.py -i $(inputVcfDir)/ -o $(releaseDir)/pipeline_output/ -p


