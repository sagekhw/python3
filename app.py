from app import *
from app.config.AppConfig import *

server_port = FlaskConfig.PORT

app.run(host="0.0.0.0", port=server_port)

