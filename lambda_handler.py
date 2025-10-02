from mangum import Mangum
from app.main import app

# Create the Mangum handler
handler = Mangum(app, lifespan="off")

def lambda_handler(event, context):
    # Call the Mangum handler
    response = handler(event, context)

    # Ensure headers dict exists
    if 'headers' not in response:
        response['headers'] = {}

    # Force add CORS headers to every response
    response['headers']['access-control-allow-origin'] = '*'
    response['headers']['access-control-allow-methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
    response['headers']['access-control-allow-headers'] = '*'

    return response