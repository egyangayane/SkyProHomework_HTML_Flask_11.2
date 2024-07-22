import json

def load_candidates_from_json(path):
    '''возвращает список всех кандидатов'''
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidate(candidate_id):
    '''возвращает одного кандидата по его id'''
    candidates = load_candidates_from_json('candidates.json')
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate
    return None

def get_candidates_by_name(candidate_name):
    '''возвращает кандидатов по имени'''
    chosen_candidates = []
    candidates = load_candidates_from_json('candidates.json')
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            chosen_candidates.append(candidate)
    return chosen_candidates

def get_candidates_by_skill(skill_name):
    '''возвращает кандидатов по навыку'''
    chosen_candidates = []
    candidates = load_candidates_from_json('candidates.json')
    for candidate in candidates:
        if skill_name.lower() in candidate['skills']:
            chosen_candidates.append(candidate)
    return chosen_candidates

