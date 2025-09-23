from mangum import Mangum
from app.main import app

# Create the Mangum handler
handler = Mangum(app, lifespan="off")

# This is the Lambda entry point
def lambda_handler(event, context):
    return handler(event, context)