test:
	pytest tests/ -s

db_setup:
	psql -d precium -f precium/database/queries/db_setup.sql