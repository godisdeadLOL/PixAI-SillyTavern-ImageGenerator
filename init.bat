If Not Exist ".venv" (
	pip install virtualenv
	python -m venv .venv
)
If Not Exist "account.txt" (
	copy NUL account.txt
)
Call .venv\Scripts\activate
pip install -r requirements.txt