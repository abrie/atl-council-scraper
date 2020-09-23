test:
	python3 -m unittest
container:
	docker build . -t abriedev/atlcouncilscraper
