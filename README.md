# Assistant Management API

This is a Flask-based RESTful API for managing assistants. It provides endpoints for creating, retrieving, updating, and deleting assistant records.

## Running the Application Locally

To run the application locally, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine.

2. **Install Dependencies**: Navigate to the project directory and install the required Python dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. **Create the SQLite Database**: Ensure that you have SQLite installed in your environment. The application expects a SQLite database file named `assistants.db` in the project directory. If the file doesn't exist, it will be created automatically when you run the application.

4. **Run the Flask Application**: Execute the following command to start the Flask application:

    ```bash
    flask run
    ```

   The application will start running on `http://127.0.0.1:5000`.

## Using the Postman Collection

Follow these steps to use the Postman collection:

1. **Import the Collection**: Import the provided Postman collection file (`Assistant_Management_API.postman_collection.json`) into your Postman application.

2. **Start the Flask Application**: Ensure that the Flask application is running locally by following the steps mentioned above.

3. **Test Endpoints**: Use the imported Postman collection to test the API endpoints. The collection includes requests for creating, retrieving, updating, and deleting assistant records. Each request contains sample JSON data for the request body where applicable.

4. **Inspect Responses**: Postman will display the response from the server for each request. You can view the status code, response headers, and response body to verify the functionality of the API endpoints.
