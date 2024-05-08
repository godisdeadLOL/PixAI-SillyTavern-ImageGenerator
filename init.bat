If Not Exist ".venv" (
	pip install virtualenv
	python -m venv .venv
)
Call .venv\Scripts\activate
pip install -r requirements.txt