# PDF Splitter

This project is a FastAPI application that allows users to upload PDF files and splits them into images of their pages. Each page of the PDF is converted into an image and saved to a specified directory.

## Features

- Upload PDF files
- Split PDF into individual page images
- Save images in specified formats

```
└── 📁pdf_splitter
    └── 📁.vscode
        └── tasks.json
    └── 📁src
        └── config.py
        └── main.py
        └── 📁models
            └── image.py
        └── 📁utils
            └── pdf_utils.py
    └── 📁tests
        └── test_main.py
    └── .dockerignore
    └── .gitignore
    └── Dockerfile
    └── README.md
    └── requirements.txt
```

## Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   cd pdf_splitter
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the FastAPI application, execute the following command:

```
uvicorn src.main:app --reload
```

You can then access the API at `http://127.0.0.1:8000`.

## API Endpoints

- **POST /upload**: Upload a PDF file to be split into images.

## Testing

To run the tests, use the following command:

```
pytest tests/test_main.py
```

## Docker

To build the Docker image, run:

```
docker build -t pdf_splitter .
```

To run the Docker container:

```
docker run -p 8000:8000 pdf_splitter
```

## License

This project is licensed under the MIT License.
