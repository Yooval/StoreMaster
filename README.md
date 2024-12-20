
## Overview
**StoreMaster** is an E-commerce RESTful API built with Python, Flask, Docker, Flask-Smorest, and Flask-SQLAlchemy. Using PostgreSQL database. The application is designed to handle users, stores, and products with CRUD operations. The application secure user authentication and autherization with JWT(Json Wen Token) management. 

All API requests documented in postmandocumented [here](https://documenter.getpostman.com/view/38510958/2sAYJ1m3KT#b130028a-058d-4d6e-9629-f03fd8694759). give it a try!

### Tech & Tools

- Docker: Used to create an isolated environment, ensuring consistency across systems.
- Flask-Smorest: Ensures accurate and consistent APIs by validating inputs and outputs using pre-defined schemas.
- Flask-sqlAlchemy:Simplify database integration by managing queries and models through an ORM layer.
## Installation
 
1. Clone the repository:
   ```
   git clone <repository_url>
   cd <repository_directory>
   ```
 
2. Ensure you have Docker Desktop installed and running on your machine.
 
3. Install Postman:
 
## Local Development
 
1. Start the application:
   ```
   docker compose up
   ```
 
2. The API will be available at `http://localhost:5000`.
 
3. Use Postman documentation to test the API endpoints [here](https://documenter.getpostman.com/view/38510958/2sAYJ1m3KT#b130028a-058d-4d6e-9629-f03fd8694759). .
 
## Deployment on Render
 
1. Set up a PostgreSQL database service on Render.
 
2. Create a new Web Service on Render:
   - Connect your GitHub repository
   - Select "Docker" as the environment
   - Set the environment variable `DATABASE_URL` to your Render PostgreSQL connection string
 
3. Deploy the service.
 
4. Once deployed, you can access your API at the URL provided by Render.
 
5. Update your Insomnia environment to use the Render URL instead of localhost.
