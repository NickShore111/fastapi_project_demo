# fastapi_project_demo

## Project Goal
- Develop an API using Python to record posts, content, users, and votes using the following modules:
  - FastAPI
  - Pydantic
  - SQLAlchemy
  - Alembic
- Use Postman Agent for testing and development
  - Setup testing environment and variables
- Database backend utilizes PostgresQL
  - Utilizes many-to-one relationship
- Deploy on Heroku and live ![here](https://fastapi-nickshore.herokuapp.com/docs)

## API Details
- Requires user creation and login
- Authentication using OAuth2 JWT Bearer token
- Utilizes Pydantic schemas for data I/O validation
