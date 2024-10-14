# StoreMaster - A Professional REST API with Python, Flask, Docker, Flask-Smorest, and Flask-SQLAlchemy


## Overview
This project is a RESTful API built with Flask, using PostgreSQL for efficient data storage and management. The API is designed to handle users, stores, and tags, allowing users to create and manage stores, with each store associated with specific items and categorized using tags. The API provides endpoints for adding, updating, and retrieving these entities, making it a flexible solution for managing structured data.

It includes secure user authentication with JWT token management, and its scalable architecture ensures smooth handling of multiple CRUD operations.

Key features include:

**User authentication**: Secure login and token-based authentication using JWT.
**Data management:** CRUD operations for users, stores, and tags.
**PostgreSQL integration:** Provides robust data persistence and management.


 
## Installation
 
1. Clone the repository:
   ```
   git clone <repository_url>
   cd <repository_directory>
   ```
 
2. Ensure you have Docker Desktop installed and running on your machine.
 
3. Install Insomnia:
   Download and install Insomnia from [Insomnia's official website](https://insomnia.rest/download).
 
## Local Development
 
1. Start the application:
   ```
   docker compose up
   ```
 
2. The API will be available at `http://localhost:5000`.
 
3. Use Insomnia to test the API endpoints.
 
## Deployment on Render
 
1. Set up a PostgreSQL database service on Render.
 
2. Create a new Web Service on Render:
   - Connect your GitHub repository
   - Select "Docker" as the environment
   - Set the environment variable `DATABASE_URL` to your Render PostgreSQL connection string
 
3. Deploy the service.
 
4. Once deployed, you can access your API at the URL provided by Render.
 
5. Update your Insomnia environment to use the Render URL instead of localhost.
