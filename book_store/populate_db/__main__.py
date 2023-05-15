import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from populate_table_command import PopulateTable # noqa
from factories import CountryFactory # noqa
from fake_lib.provider import CountryProvider # noqa
from data_access.dao import CountryDAO # noqa
from data_access import SqliteGateway # noqa

AVAILABLE_FLAGS = ("-d", "-n")

if __name__ == "__main__":
    config_args = sys.argv[1:]
    for index in range(0, len(config_args), 2):
        flag = config_args[index]
        if flag not in AVAILABLE_FLAGS:
            raise ValueError("Invalid flag")
        elif flag == "-d":
            db_name = config_args[index + 1]
        elif flag == "-n":
            records_number = int(config_args[index + 1])

    db_gateway = SqliteGateway(db_name=db_name)

    country_dao = CountryDAO(db_gateway=db_gateway)
    country_factory = CountryFactory(country_provider=CountryProvider())
    PopulateTable(
        records_number=records_number,
        dao=country_dao,
        fake_factory=country_factory
    ).execute()
