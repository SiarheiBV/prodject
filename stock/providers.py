from data_access import JSONStorage


def provide_db(db_type, db_file):

    if db_type == "json":
        return JSONStorage(db_file)
    else:
        raise ValueError("Unsupported DB type.")
