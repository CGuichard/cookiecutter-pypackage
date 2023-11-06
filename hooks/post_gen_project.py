{% if cookiecutter.git_init %}
import subprocess

# Git init
subprocess.call(["git", "init", "--initial-branch", "{{ cookiecutter.git_branch }}"])
subprocess.call(["git", "remote", "add", "origin", "git@github.com:{{ cookiecutter.git_user }}/{{ cookiecutter.project_slug }}.git"])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "chore: initial commit"])
{% endif %}
