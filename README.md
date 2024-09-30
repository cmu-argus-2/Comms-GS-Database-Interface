
# Comms-GS-Database-Interface

This interface provides Python scripts and classes to interact with Google Cloud Storage, allowing you to upload, download, and list files from a GCS bucket. 

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Uploading a File](#uploading-a-file)
  - [Downloading a File](#downloading-a-file)
  - [Listing Files in the Bucket](#listing-files-in-the-bucket)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Requirements

- Python 3.x
- Google Cloud SDK
- Google Cloud Storage Python Client Library (`google-cloud-storage`)

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install dependencies**:

   Install the required Python libraries:
   
   ```bash
   pip install google-cloud-storage
   ```

3. **Set up Google Cloud SDK**:

   If you haven't already, install the Google Cloud SDK and authenticate:

   ```bash
   gcloud auth application-default login
   ```

## Configuration

1. **Google Cloud Credentials**:

   You must have a Google Cloud Service Account key. Once you have downloaded the JSON key file, set it up in your environment:

   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/key.json"
   ```

   Alternatively, you can use the following in your Python code:

   ```python
   import os
   os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/key.json"
   ```

2. **Bucket Setup**:

   Ensure that you have access to a Google Cloud Storage bucket. You will need the bucket name to interact with it.

## Usage

### Uploading a File

To upload a file to a Google Cloud Storage bucket, use the `GoogleCloudUploader` class or the `upload_file_to_bucket` function.

**Example**:

```python
from google.cloud import storage
from uploader import GoogleCloudUploader

# Initialize uploader with your bucket name
uploader = GoogleCloudUploader(bucket_name="your-bucket-name")

# Upload a file
uploader.upload_image("path/to/local/image.png", "remote/path/image.png")
```

Alternatively, you can upload a file using the `upload_file_to_bucket` function:

```python
from uploader import upload_file_to_bucket

# Upload a file using gs:// URI
upload_file_to_bucket('gs://your-bucket-name/path/image.png', 'local/path/image.png')
```

### Downloading a File

To download a file from the bucket:

```python
uploader.download_from_bucket('remote/path/image.png', 'local/path/to/save/image.png')
```

### Listing Files in the Bucket

To list all the files in your Google Cloud Storage bucket:

```python
uploader.list_images()
```

## Error Handling

The project contains basic error handling for issues like invalid Google Cloud credentials, missing files, or permission errors. If you encounter an error such as insufficient permissions, ensure that your service account or credentials have the appropriate access to the bucket.

For more detailed logging, consider enabling logging within the Python script.

## Contributing

We welcome contributions! Feel free to submit a pull request or open an issue for any improvements, features, or bugs.

1. Fork the repo.
2. Create your feature branch: `git checkout -b my-new-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-new-feature`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
