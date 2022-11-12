test:
	pytest tests/ -s

db_setup:
	psql -d precium -f precium/database/psql/queries/db_setup.sql