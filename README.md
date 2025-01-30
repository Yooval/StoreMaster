
## Overview

**StoreMaster** is an e-commerce REST API application built with Flask. It allows users to manage accounts, stores, and products. The application includes secure login and access controls to protect user information and ensure safety.

### Tech & Tools

- **Flask-Smorest**: Ensures accurate and consistent APIs by validating inputs and outputs using pre-defined schemas.
- **Flask-SQLAlchemy**: Simplifies database integration by managing queries and models through an ORM layer.
- **Redis**: Enhances performance by caching frequently accessed data.
- **Docker**: Creates an isolated environment, ensuring consistency across systems.

### Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. Run the command:  
   ```bash
   docker run -p 5000:80 <container_name>
   ```

3. The API will be available at `http://localhost:5000`.

4. Use tools like Postman to test the API endpoints.
