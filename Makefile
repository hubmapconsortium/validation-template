OUTPUTDIR = ../output

.PHONY: reports
reports: validation-config.yml
	python src/validation.py --config validation-config.yml


$(OUTPUTDIR)/%/graph.png: $(OUTPUTDIR)/%/ont.owl
	$(ROBOT) annotate --input $< --ontology-iri http://purl.org/ccf/latest/$*/ont.owl convert -o $*.json && \
	og2dot.js -s ../style/ubergraph-style.json $*.json > $*.dot && \
	dot $*.dot -Tpng -Grankdir=LR > $@ && \
	rm $*.json && \
	rm $*.dot