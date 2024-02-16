.PHONY: reports
reports: validation-config.yml
	python src/validation.py --config validation-config.yml