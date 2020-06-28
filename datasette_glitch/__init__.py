from datasette import hookimpl
import os


@hookimpl
def startup(datasette):
    domain = os.environ.get("PROJECT_DOMAIN")
    if domain:
        print(
            "https://{}.glitch.me/-/auth-token?token={}".format(
                domain, datasette._root_token
            )
        )
