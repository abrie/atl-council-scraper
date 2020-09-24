dependencies:
	pip3 install -r requirements.txt

test:
	python3 -m unittest

container:
	docker build . -t abriedev/atl-council-scraper
