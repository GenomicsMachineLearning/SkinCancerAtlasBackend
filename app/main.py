import fastapi as fastapi
import fastapi.middleware.cors as fastapi_middleware_cors
import app as app
import app.routers.health as app_routers_health
import app.routers.samples as app_routers_samples
import app.routers.scrnaseq as app_routers_scrnaseq
from app.core.config import settings

# Create FastAPI application
app = fastapi.FastAPI(
    title=app.core.config.settings.PROJECT_NAME,
    description="FastAPI Skin Cancer Atlas Backend Service",
    version="1.0.0",
    docs_url="/docs" if app.core.config.settings.ENVIRONMENT != "production" else None,
    redoc_url="/redoc" if app.core.config.settings.ENVIRONMENT != "production" else None,
)

# Add CORS middleware
app.add_middleware(
    fastapi_middleware_cors.CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(app_routers_health.router, prefix="/health", tags=["health"])
app.include_router(app_routers_samples.router, tags=["api"])
app.include_router(app_routers_scrnaseq.router, tags=["api"])


@app.get("/")
async def root():
    return {"message": "FastAPI Lambda Service"}
