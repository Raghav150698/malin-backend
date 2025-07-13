
def rank_responses(responses):
    # Very basic ranking based on length for now
    return sorted(responses, key=lambda x: len(x['text']), reverse=True)
