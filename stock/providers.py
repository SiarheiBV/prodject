from data_access import JSONStorage


def provide_db(db_type: str, db_file: str) -> JSONStorage | None:

    if db_type == "json":
        return JSONStorage(db_file)
    else:
        raise ValueError("Unsupported DB type.")
