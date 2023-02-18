from app.cafe import Cafe
from app.errors import OutdatedVaccineError
from app.errors import NotVaccinatedError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    vaccines = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotWearingMaskError:
            masks_to_buy += 1
        except (NotVaccinatedError, OutdatedVaccineError):
            vaccines += 1
    if vaccines > 0:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
