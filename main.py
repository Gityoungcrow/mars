from flask import Flask
from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/mars_explorer.db')
    db_sess = db_session.create_session()
    jobs = Jobs(job="deployment of residential modules 1 and 2", work_size=15, collaborators='2, 3',
                team_leader=1, is_finished=False)
    db_sess.add(jobs)
    db_sess.commit()
    # app.run()


if __name__ == "__main__":
    main()