from fastapi import FastAPI
from models import user_model,role_model
from configurations import engine
from fastapi.middleware.cors import CORSMiddleware
from routes import (
        role_route as role,
        user_route as user
    )


#initializing app
app = FastAPI()


origins = ["*"]

# If you want to allow specific origins, you can do:
# origins = ["http://localhost:3000", "https://your-frontend-domain.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# routers
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(role.router, prefix="/roles", tags=["roles"])


user_model.Base.metadata.create_all(bind=engine)
role_model.Base.metadata.create_all(bind=engine)
