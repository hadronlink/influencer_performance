# Influencer Connectus

Influencer Connectus is a web application designed to track and display the performance of influencers. The application provides a dashboard where influencers can view metrics such as new users, conversion rates, and trends over time. The application is built using Flask and includes features such as date range filtering and data visualization with Chart.js.

## Project Description

This project aims to provide a comprehensive dashboard for influencers to monitor their performance. The dashboard includes:
- Metrics for new users and conversion rates.
- Trend charts to visualize user growth over time.
- A timeline of posts created by the influencer.

## Running the Application

To run the application locally, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/influencer_connectus.git
    cd influencer_connectus
    ```

2. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Flask application:**
    ```sh
    python app.py
    ```

The application will be available at `http://localhost:5000`.

## Docker Deployment

To deploy the application using Docker, follow these steps:

1. **Build the Docker image:**
    ```sh
    docker build -t influencer_connectus .
    ```

2. **Run the Docker container:**
    ```sh
    docker run -p 5000:5000 influencer_connectus
    ```

The application will be available at `http://localhost:5000`.

## Tagging and Pushing the Docker Image

To tag and push the Docker image to a Docker registry, follow these steps:

1. **Tag the Docker image:**
    ```sh
    docker tag influencer_connectus santoshadronlink/influencer_connectus:latest
    ```

2. **Push the Docker image:**
    ```sh
    docker push santoshadronlink/influencer_connectus:latest
    ```



## Health Check

The Dockerfile includes a health check to ensure the application is running. The health check is configured to run every 30 seconds, with a timeout of 10 seconds, and will retry up to 3 times.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
