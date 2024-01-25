OUTPUTDIR = ../output

$(OUTPUTDIR)/report/%.tsv: validation-config.yml
	python src/validation.py --config validation-config.yml


$(OUTPUTDIR)/graph/%.png: $(OUTPUTDIR)/owl/%.owl
	og2dot.js -s ../style/ubergraph-style.json $*_f.json > $*.dot && \
	dot $*.dot -Tpng -Grankdir=LR > ../graphs/ccf_$*_graph.png && \
	rm $*.json && \
	rm $*_sec_reduced.json && \
	rm $*_f.json && \
	rm $*.dot; fi