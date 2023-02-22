from api import create_app
import config

app = create_app(config.DevConfig)
