"""
Githubscore Repo Leaderboard

URLs include:
/repoboard
"""
import flask
import githubscore
import requests

from githubscore.model import get_db


# TO DO:
@githubscore.app.route('/repoboard', methods = ["GET"])
def show_repoboard():
    """Display / route."""
    # username = 'nwchinn'
    # response = requests.get("https://api.github.com/users/" + username)
    # user_data = response.json()
    # print(user_data)
    # print('Name: ', user_data['name'])
    # print('login: ', user_data['login'])
    # print('Followers: ', user_data['followers'])
    # print('Following: ', user_data['following'])
    # print('Public Repos: ', user_data['public_repos'])


    context = {}

    db = get_db()
    cur = db.cursor()
    top_repos = cur.execute('''SELECT full_name, stargazers_count, watchers_count, forks_count FROM repos ORDER BY stargazers_count DESC''').fetchall()

    print(top_repos)
    context['repos'] = top_repos

    # for repo in user_repos:
    #     print(repo['login'],repo['public_repos'])
    #     context['data'].append(repo['public_repos'])


    # context['login'] = user_data['login']
    # context['login'] = 'LEADERBOARD'

    # context['']
    return flask.render_template("repoboard.html", **context)


# @githubscore.app.route("/data")
#     def data():



#         return jsonify(get_data())
