from quart import Quart, jsonify
import structlog
import uuid


def create_app(configuration):

    logger = structlog.get_logger()

    logger.info(msg="Initializing app")
    app = Quart(__name__)

    @app.route("/", methods=["GET"])
    async def home():

        log = logger.new(request_id=str(uuid.uuid4()))

        log.info("here we go again")

        payload = {"msg": "Yeah I'm working!"}

        return jsonify(payload)

    logger.info("Running app")

    return app
