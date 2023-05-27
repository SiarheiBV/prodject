from populate_table_command import PopulateTable
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from factories import (CountryFactory,# noqa
                       AuthorsFactory,# noqa
                       UsersFactory,# noqa
                       RolesFactory,# noqa
                       PermissionsFactory,# noqa
                       BooksFactory,# noqa
                       GenresFactory,# noqa
                       UsersRolesFactory,# noqa
                       RolesPermFactory,# noqa
                       BasketsBooksFactory,# noqa
                       BasketsFactory,# noqa
                       BooksAuthorsFactory,# noqa
                       BooksGenresFactory,# noqa
                       CitiesFactory,# noqa
                       AddressFactory,# noqa
                       TransactionsFactory,# noqa
                       BankCardFactory)  # noqa
from data_access.dao import (CountryDAO,# noqa
                             AuthorsDAO,# noqa
                             UsersDAO,# noqa
                             RolesDAO,# noqa
                             PermissionsDAO,# noqa
                             BooksDAO,# noqa
                             GenresDAO,# noqa
                             UsersRolesDAO,# noqa
                             RolesPermDAO,# noqa
                             BasketsDAO,# noqa
                             BasketsBooksDAO,# noqa
                             BooksAuthorsDAO,# noqa
                             BooksGenresDAO,# noqa
                             CitiesDAO,# noqa
                             AddressDAO,# noqa
                             TransactionsDAO,# noqa
                             BankCardsDAO)  # noqa
from data_access import SqliteGateway  # noqa
from fake_lib.provider import (CountryProvider,# noqa
                               NameProvider,# noqa
                               SurnameProvider,# noqa
                               DateProvider,# noqa
                               InfoProvider,# noqa
                               PasswordProvider,# noqa
                               AgeProvider,# noqa
                               NicknameProvider,# noqa
                               EmailProvider,# noqa
                               PhoneProvider,# noqa
                               RolesProvider,# noqa
                               PermissionsProvider,# noqa
                               BooksProvider,# noqa
                               PriceProvider,# noqa
                               AuthorsProvider,# noqa
                               PageProvider,# noqa
                               FormatProvider,# noqa
                               AgeRestrictionProvider,# noqa
                               RandomIntProvider,# noqa
                               GenresProvider,# noqa
                               RandomChoiceProvider,# noqa
                               StatusProvider,# noqa
                               CitiesProvider,# noqa
                               PostCodeProvider,# noqa
                               AddressProvider,# noqa
                               CVCProvider,# noqa
                               BankCardProvider,# noqa
                               ExpirationProvider)  # noqa

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

    country_list = country_dao.get_ids_list()

    author_dao = AuthorsDAO(db_gateway=db_gateway)
    author_factory = AuthorsFactory(name_provider=NameProvider(),
                                    surname_provider=SurnameProvider(),
                                    b_date_provider=DateProvider(),
                                    d_date_provider=DateProvider(),
                                    info_provider=InfoProvider())

    PopulateTable(
        records_number=records_number,
        dao=author_dao,
        fake_factory=author_factory
    ).execute()

    author_list = author_dao.get_ids_list()

    users_dao = UsersDAO(db_gateway=db_gateway)
    users_factory = UsersFactory(name_provider=NameProvider(),
                                 surname_provider=SurnameProvider(),
                                 nikname_provider=NicknameProvider(),
                                 email_provider=EmailProvider(),
                                 age_provider=AgeProvider(),
                                 password_provider=PasswordProvider(),
                                 phone_provider=PhoneProvider())

    PopulateTable(
        records_number=records_number,
        dao=users_dao,
        fake_factory=users_factory
    ).execute()

    users_list = users_dao.get_ids_list()

    roles_dao = RolesDAO(db_gateway=db_gateway)
    roles_factory = RolesFactory(roles_provider=RolesProvider())
    PopulateTable(
        records_number=records_number,
        dao=roles_dao,
        fake_factory=roles_factory
    ).execute()

    roles_list = roles_dao.get_ids_list()

    permissions_dao = PermissionsDAO(db_gateway=db_gateway)
    permissions_factory = PermissionsFactory(permissions_provider=PermissionsProvider())
    PopulateTable(
        records_number=records_number,
        dao=permissions_dao,
        fake_factory=permissions_factory
    ).execute()

    permissions_list = permissions_dao.get_ids_list()

    books_dao = BooksDAO(db_gateway=db_gateway)
    books_factory = BooksFactory(title_provider=BooksProvider(),
                                 price_provider=PriceProvider(),
                                 descriptions_provider=InfoProvider(),
                                 author_provider=AuthorsProvider(),
                                 pages_provider=PageProvider(),
                                 format_provider=FormatProvider(),
                                 age_restriction_provider=AgeRestrictionProvider(),
                                 available_provider=RandomIntProvider())
    PopulateTable(
        records_number=records_number,
        dao=books_dao,
        fake_factory=books_factory
    ).execute()

    books_list = books_dao.get_ids_list()

    genres_dao = GenresDAO(db_gateway=db_gateway)
    genres_factory = GenresFactory(genres_provider=GenresProvider(),
                                   descriptions_provider=InfoProvider())

    PopulateTable(
        records_number=records_number,
        dao=genres_dao,
        fake_factory=genres_factory
    ).execute()

    genres_list = genres_dao.get_ids_list()

    users_roles_dao = UsersRolesDAO(db_gateway=db_gateway)
    users_roles_factory = UsersRolesFactory(users_id_provider=RandomChoiceProvider(users_list),
                                            roles_id_provider=RandomChoiceProvider(roles_list))

    PopulateTable(
        records_number=records_number,
        dao=users_roles_dao,
        fake_factory=users_roles_factory
    ).execute()

    roles_perm_dao = RolesPermDAO(db_gateway=db_gateway)
    roles_perm_factory = RolesPermFactory(roles_id_provider=RandomChoiceProvider(roles_list),
                                          perm_id_provider=RandomChoiceProvider(permissions_list))

    PopulateTable(
        records_number=records_number,
        dao=roles_perm_dao,
        fake_factory=roles_perm_factory
    ).execute()

    basket_dao = BasketsDAO(db_gateway=db_gateway)
    basket_factory = BasketsFactory(user_id_provider=RandomChoiceProvider(users_list),
                                    status_provider=StatusProvider())

    PopulateTable(
        records_number=records_number,
        dao=basket_dao,
        fake_factory=basket_factory
    ).execute()
    baskets_list = basket_dao.get_ids_list()

    books_authors_dao = BooksAuthorsDAO(db_gateway=db_gateway)
    books_author_factory = BooksAuthorsFactory(authors_id_provider=RandomChoiceProvider(author_list),
                                               books_id_provider=RandomChoiceProvider(books_list))

    PopulateTable(
        records_number=records_number,
        dao=books_authors_dao,
        fake_factory=books_author_factory
    ).execute()

    books_genres_dao = BooksGenresDAO(db_gateway=db_gateway)
    books_genres_factory = BooksGenresFactory(genres_id_provider=RandomChoiceProvider(genres_list),
                                              book_id_provider=RandomChoiceProvider(books_list))

    PopulateTable(
        records_number=records_number,
        dao=books_genres_dao,
        fake_factory=books_genres_factory
    ).execute()

    baskets_books_dao = BasketsBooksDAO(db_gateway=db_gateway)
    baskets_books_factory = BasketsBooksFactory(baskets_id_provider=RandomChoiceProvider(baskets_list),
                                                books_id_provider=RandomChoiceProvider(books_list))

    PopulateTable(
        records_number=records_number,
        dao=baskets_books_dao,
        fake_factory=baskets_books_factory
    ).execute()

    cities_dao = CitiesDAO(db_gateway=db_gateway)
    cities_factory = CitiesFactory(cities_provider=CitiesProvider(),
                                   country_id_provider=RandomChoiceProvider(country_list))

    PopulateTable(
        records_number=records_number,
        dao=cities_dao,
        fake_factory=cities_factory
    ).execute()

    citi_list = cities_dao.get_ids_list()

    address_dao = AddressDAO(db_gateway=db_gateway)
    address_factory = AddressFactory(citi_id_provider=RandomChoiceProvider(citi_list),
                                     street_provider=AddressProvider(),
                                     house_number_provider=RandomIntProvider(),
                                     postal_code_provider=PostCodeProvider(),
                                     user_id_provider=RandomChoiceProvider(users_list))

    PopulateTable(
        records_number=records_number,
        dao=address_dao,
        fake_factory=address_factory
    ).execute()

    address_list = address_dao.get_ids_list()

    bankcard_dao = BankCardsDAO(db_gateway=db_gateway)
    bankcard_factory = BankCardFactory(cart_number_provider=BankCardProvider(),
                                       first_name_provider=NameProvider(),
                                       last_name_provider=SurnameProvider(),
                                       cvc_code_provider=CVCProvider(),
                                       expiration_provider=ExpirationProvider(),
                                       user_id_provider=RandomChoiceProvider(users_list)
                                       )

    PopulateTable(
        records_number=records_number,
        dao=bankcard_dao,
        fake_factory=bankcard_factory
    ).execute()

    bankcard_list = bankcard_dao.get_ids_list()

    transactions_dao = TransactionsDAO(db_gateway=db_gateway)
    transactions_factory = TransactionsFactory(basket_id_provider=RandomChoiceProvider(baskets_list),
                                               bankcard_id_provider=RandomChoiceProvider(bankcard_list),
                                               amoutd_provider=RandomIntProvider(),
                                               address_id_provider=RandomChoiceProvider(address_list))

    PopulateTable(
        records_number=records_number,
        dao=transactions_dao,
        fake_factory=transactions_factory
    ).execute()
