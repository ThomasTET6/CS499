"""
MongoDB query definitions.

This module stores the rescue type queries used by the dashboard.

Future enhancements:
- Replace static query definitions with a dynamic query builder.
- Improve query efficiency for larger datasets.
- Reduce repeated filtering logic through reusable functions.
"""


WATER_QUERY = {
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
}


MOUNTAIN_QUERY = {
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
}


DISASTER_QUERY = {
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