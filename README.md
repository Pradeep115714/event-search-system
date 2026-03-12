# Event Search System

The Event Search System is a web application built using Django REST API and HTML/JavaScript.  
It allows users to search events from multiple CSV files based on event name and time range.

---

## Features

- Search events using a keyword
- Filter events by start time and end time
- Read event data from CSV files
- Display results with event name, time, and source file
- Show search execution time

---

## Technologies Used

- Python
- Django
- Django REST Framework
- HTML
- JavaScript
- CSV Data Files

---

## Project Structure

backend
│
├── api
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── apps.py
│
├── data_files
│   ├── events1.csv
│   └── events2.csv
│
├── myproject
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates
│   └── index.html
│
├── manage.py
└── db.sqlite3

---

## How to Run the Project

1. Install dependencies

```bash
pip install -r requirements.txt

## Results

### Event Search Page

[Event Search](results.jpeg)
