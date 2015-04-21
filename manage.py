#!/usr/bin/env python

"""
    Manage.py
    =========

    Manager script for teh data_vis project.

    Can start up a server instance, run analyses and purge database records.
"""

from pathlib import Path

from flask.ext.script import Manager

from data_vis import app
from data_vis.models import get_session, Faculty


manager = Manager(app)


@manager.command
def reset_db():
    """ Initialise the database tables.
    """
    db_file = Path('courses.db')

    # Delete database file
    if db_file.exists():
        print('SQLite file exists, removing it.')
        db_file.unlink()
    else:
        print('No SQLite file found.')

    session = get_session()

    # Load Faculties.
    faculty_info = [
        ('BEL', 'Business, Economics and Law'),
        ('EAIT', 'Engineering, Architecture and Information Technology'),
        ('HABS', 'Health and Behavioural Sciences'),
        ('HASS', 'Humanities and Social Sciences'),
        ('MBS', 'Medicine and Biomedical Sciences'),
        ('SCI', 'Science'),
    ]
    # Add faculties to the database.
    for fac_id, title in faculty_info:
        fac_obj = Faculty(id=fac_id, title=title)
        print('Adding {} to database'.format(fac_obj))
        session.add(fac_obj)
    session.commit()


@manager.command
def run_debug():
    """
    Run a debug server.
    """
    app.run(debug=True)


if __name__ == "__main__":
    manager.run()
