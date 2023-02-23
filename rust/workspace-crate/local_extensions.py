from jinja2.ext import Extension
import subprocess


class GithubRepoNameExtension(Extension):
    """Jinja2 Extension to get the Github repo name of the current git repo.

    The Githb repo name is the `REPO` portion of
    `https://github.com:<OWNER>/<REPO>` or `git@github.com:<OWNER>/<REPO>.git`
    """

    def __init__(self, environment):
        super().__init__(environment)

        def github_repo_name():
            output = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True)
            if output.returncode != 0:
                return "repo_name"

            # The repository should be of the form:
            #
            #   "git@github.com:<OWNER>/<REPO>.git"
            #
            # We want to return the <REPO> So we will split at the last "/" and
            # remove the ".git" ending.
            output = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True)
            name_with_extension = output.stdout.rsplit(b"/")[1]
            name = name_with_extension.split(b".git")[0]
            return name.decode("utf-8")

        environment.globals.update(github_repo_name=github_repo_name)

class GithubUsernameExtension(Extension):
    """Jinja2 Extension to get the current Github username via `gh`.
    """

    def __init__(self, environment):
        super().__init__(environment)

        def github_username():
            output = subprocess.run(["gh", "api", "user"], capture_output=True)
            if output.returncode != 0:
                return ""

            user = json.loads(output.stdout)
            return user["login"]

        environment.globals.update(github_username=github_username)

