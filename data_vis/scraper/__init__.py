# from ..models import get_session
from . import programs, majors
from data_vis import models

def scrape_programs():
    """

    :return:
    """
    session = models.get_session()

    program_ids = programs.find_program_ids()
    page_sources = programs.harvest_program_pages(program_ids)
    programs.analyse_webpages(page_sources, session)

    session.commit()


def scrape_majors():
    """

    :return:
    """
    major_ids = majors.get_major_ids()
    major_sources = majors.harvest_majors(major_ids)
    major_rows = majors.process_pages(major_sources)
    majors.add_programs_to_db(major_rows)
