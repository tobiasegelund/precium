test:
	pytest tests/ -s

db_setup:
	psql -d precium -f database/psql/queries/db_setup.sql