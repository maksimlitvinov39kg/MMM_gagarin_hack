import typing as tp
from funcs import *
EntityScoreType = tp.Tuple[int, float]  # (entity_id, entity_score)
MessageResultType = tp.List[
    EntityScoreType
]  # list of entity scores,
#    for example, [(entity_id, entity_score) for entity_id, entity_score in entities_found]


def score_texts(messages):
    scores = []
    for message in messages:
        scores.append(get_all_from_text(message))
    return scores
