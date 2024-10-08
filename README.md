![Screen Shot 2023-12-13 at 07 04 01 PM](https://github.com/JonathanGarro/rc-select/assets/8890661/ca9e5876-7d8f-41fa-b6b7-e2619e881fc0)

RC Select is a tool to help program and emergency response teams choose the right solution for their data management needs. A catalogue of vetted options gives users an honest picture of the pros and cons of each option, and a self-guided tool picker translates program needs into technical requirements.

## Installation

To install the app locally, you will need a local PostreSQL server. The deployment expects the environment variables DB_HOSTNAME and DB_PASSWORD to point to this instance. The Django migrations script will create the necessary database structures for an initial state.

### To deploy locally

1. Set `DEBUG` appropriately in `settings.py`.If deploying to production, set `DEBUG=False`.

2. Add your host to `ALLOWED_HOSTS` to avoid CRSF errors.

3. Run `python manage.py collectstatic` to gather static files.

4. Create a python virtual environment and install required python modules.

```python
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
5. Run the database migrations to create database structures

```python
python manage.py migrate
```

6. Create an administrative user for the application. This step is needed before you can attempt to import data.

```python
python manage.py createsuperuser
```

7. Run the application

```python
python manage.py runserver
```

# Loading data

There is a sample set of data in the `seed_data` subdirectory that can be loaded directly to the database tables via your favorite SQL tool (e.g. DBeaver). Please note that this sample data is incomplete and is provided to help illustrate potential capabilities of the tool.

Following is a good order to load the tables:

1. tool_picker_language.csv
2. tool_picker_tool.csv
3. tool_picker_tool_languages.csv
4. tool_picker_toolfeature.csv
5. tool_picker_tool_tool_features.csv
6. tool_picker_toolresource.csv
7. tool_picker_tool_tool_resources.csv
8. tool_picker_tool_tool_resources.csv
9. tool_picker_toolattributedefinition.csv
10. tool_picker_toolpickerresponses.csv
