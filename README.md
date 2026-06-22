REST API Fundamentals
This repository serves as an educational foundation for building RESTful APIs. It demonstrates how to handle standard HTTP methods, implement data validation, and return structured JSON responses using Python (Flask) and Node.js (Express).

Project Description
This project focuses on the core mechanics of REST API development. It includes a functional local server implementation that manages a collection of products. By following this implementation, you will learn how to:

Set up a local development server.

Define RESTful routes (GET and POST).

Validate client requests to ensure data integrity.

Return consistent JSON-formatted responses.

Topics Covered
REST API Basics: Understanding how web resources are requested and managed via HTTP.

Flask Routing: Defining URL endpoints using @app.route.

Request Handling: Parsing incoming JSON payloads and handling errors gracefully.

HTTP Status Codes: Using appropriate status codes like 200 OK, 201 Created, and 400 Bad Request to communicate server responses.

JSON Serialization: Converting Python/JavaScript objects into structured JSON for client-server communication.

How to Run
Clone the repository: git clone <your-repo-url>

Install dependencies: pip install flask (for Python) or npm install express (for Node.js).

Run the server:

Python: python app.py.

Test the endpoints: Use Postman or curl to send GET requests to /products and POST requests with a JSON body containing name and price.

Created as part of the fundamentals for REST API development.
