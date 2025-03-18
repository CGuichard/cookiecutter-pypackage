{% if cookiecutter.git_init %}
import subprocess

# Git init
subprocess.call(["git", "init", "--initial-branch", "{{ cookiecutter.git_branch }}"])
subprocess.call(["git", "remote", "add", "origin", "{{ cookiecutter.__git_repo_origin }}"])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "chore: initial commit"])
{% endif %}
