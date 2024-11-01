# kpi_data_processing_engine
Project Setup and Execution Guide

1. Running the Interpreter from main.py

	•	Usage: This script reads messages from messages.txt, processes each using configured equations in equation_config.json, and inserts results into the database.
	•	Command:

python main.py



2. Running Tests in tests.py

	•	Usage: This runs unit tests for core functionality, including arithmetic and regex expression evaluation.
	•	Command:

python tests.py



3. Running the KPI Django App

	•	Navigate to the KPI app directory and start the Django development server.
	•	Commands:

python manage.py migrate
python manage.py runserver


	•	Endpoints:
	•	POST /api/kpis/: Add a new KPI.
	•	GET /api/kpis/: List KPIs.
	•	POST /api/asset-kpis/: Link an asset to a KPI.
