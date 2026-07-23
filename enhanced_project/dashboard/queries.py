"""
Query definitions used by the dashboard.

This module centralizes all rescue filter logic so queries can be
generated dynamically instead of using large if/elif chains.

Future enhancements:
- Load rescue criteria from a configuration file or database.
- Allow users to create custom rescue filters.
"""

RESCUE_FILTERS = {
    "WATER": {
        "animal_type": "Dog",
        "breed": {
            "$regex": "Labrador Retriever Mix|Chesapeake Bay Retriever|Newfoundland",
            "$options": "i"
        },
        "sex_upon_outcome": "Intact Female",
        "age_upon_outcome_in_weeks": {
            "$gte": 26,
            "$lte": 156
        }
    },

    "MOUNTAIN": {
        "animal_type": "Dog",
        "breed": {
            "$regex": "German Shepherd|Alaskan Malamute|Old English Sheepdog|Siberian Husky|Rottweiler",
            "$options": "i"
        },
        "sex_upon_outcome": "Intact Male",
        "age_upon_outcome_in_weeks": {
            "$gte": 26,
            "$lte": 156
        }
    },

    "DISASTER": {
        "animal_type": "Dog",
        "breed": {
            "$regex": "Doberman Pinscher|German Shepherd|Golden Retriever|Bloodhound|Rottweiler",
            "$options": "i"
        },
        "sex_upon_outcome": "Intact Male",
        "age_upon_outcome_in_weeks": {
            "$gte": 20,
            "$lte": 300
        }
    }
}


def build_query(filter_type):
    """
    Return the MongoDB query associated with the selected rescue type.

    Parameters
    ----------
    filter_type : str
        The selected rescue filter.

    Returns
    -------
    dict
        MongoDB query for the selected rescue type.
        Returns an empty dictionary when no filter is selected.
    """
    return RESCUE_FILTERS.get(filter_type, {})