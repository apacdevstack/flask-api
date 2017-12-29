# FlaskSample

### Run Application
* Install the dependencies first using the command `pip install -r requirements.txt`
* Then run the application using `python app.py` which will start a development server at `127.0.0.1:8080`

### Run Tests

* This project is configured to run test-suites using `pytest` framework.
* To run tests, simply enter the command `py.test`

### Build Docker Image

* Use `docker build -t FlaskSample .` to build the Docker Image
* You can the run the image using the command `docker run -it -p 8080:8080 FlaskSample` 