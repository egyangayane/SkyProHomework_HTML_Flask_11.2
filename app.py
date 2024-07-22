from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

candidates = load_candidates_from_json("candidates.json")

@app.route('/')
def index():
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:candidate_id>')
def candidate(candidate_id):
    candidate = get_candidate(candidate_id)
    if candidate:
        return render_template('single.html', candidate=candidate)
    return "Кандидат не найден", 404

@app.route('/search/<candidate_name>')
def search(candidate_name):
    candidates_found = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates_found)

@app.route('/skill/<skill_name>')
def skill(skill_name):
    candidates_found = get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates_found)

app.run(debug=True)
