from typing import List

from data.cages import Cage
from data.owners import Owner


def create_account(name: str, email: str) -> Owner:
    owner = Owner()
    owner.name = name
    owner.email = email

    owner.save()

    return owner


def find_account_by_email(email: str) -> Owner:
    # owner = Owner.objects().filter(email=email).first()
    owner = Owner.objects(email=email).first()  # for one filer, we can directly do this in mongodb
    return owner


def register_cage(active_account: Owner, price, name,
                  allow_dangerous, has_toys, carpated, meters) -> Cage:
    cage = Cage()
    cage.name = name
    cage.allow_dangerous_snakes = allow_dangerous
    cage.is_carpeted = carpated
    cage.has_toys = has_toys
    cage.price = price
    cage.square_meters = meters

    cage.save() # must save the cage data first

    account = find_account_by_email(active_account.email)
    account.cage_ids.append(cage.id)
    account.save()

    return cage


def find_cages_for_user(account: Owner) -> List[Cage]:
    query = Cage.objects(id__in=account.cage_ids) # __ means $ in mongodb

    cages = list(query)

    return cages