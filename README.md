# NLP Bug Severity Predictor

This project uses Natural Language Processing (NLP) to predict the severity of software bugs based on their descriptions.

I am using kaggle dataset 

https://www.kaggle.com/datasets/krooz0/cve-and-cwe-mapping-dataset?resource=download

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/nlp-bug-severity-predictor.git
   cd nlp-bug-severity-predictor
   ```

2. Build the Docker image:
   ```
   docker build -t bug-severity-predictor .
   ```

3. Run the Docker container:
   ```
   docker run -p 8000:8000 bug-severity-predictor
   ```

## Usage

Once the server is running, you can make predictions using the `/predict` endpoint:

```
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"description":"Application crashes when uploading large files"}'
```

## Running Tests

To run the tests:

```
python tests/test_main.py
```

## License

This project is licensed under the Apache License.