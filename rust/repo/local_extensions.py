from jinja2.ext import Extension
import subprocess
import json

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

