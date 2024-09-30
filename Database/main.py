from google.cloud import storage
import os

class GoogleCloudUploader:
    def __init__(self, bucket_name):
        # Initialize the Google Cloud Storage client
        self.storage_client = storage.Client()
        self.bucket_name = bucket_name
        self.bucket = self.storage_client.bucket(bucket_name)

    # Function to upload file using gs:// URI
    def upload_file_to_bucket(self,gs_uri, source_file_name):
        """Uploads a file to the specified gs:// URI."""
        gs_prefix = "gs://"
        if not gs_uri.startswith(gs_prefix):
            raise ValueError(f"Invalid gs:// URI: {gs_uri}")
        bucket_name, destination_blob_name = gs_uri[len(gs_prefix):].split("/", 1)
        # Initialize the Google Cloud Storage client
        storage_client = storage.Client()
        # Get the bucket object
        bucket = storage_client.bucket(bucket_name)
        # Create a blob object from the destination path in the bucket
        blob = bucket.blob(destination_blob_name)
        # Upload the file to the bucket
        blob.upload_from_filename(source_file_name)
        print(f"File {source_file_name} uploaded to {gs_uri}.")
    def upload_image(self, image_path, destination_blob_name):
        """Uploads an image to the specified bucket in Google Cloud Storage."""
        try:
            blob = self.bucket.blob(destination_blob_name)
            blob.upload_from_filename(image_path)
            print(f"Image {image_path} uploaded to {destination_blob_name}.")
        except Exception as e:
            print(f"An error occurred: {e}")
            raise

    def list_images(self):
        """List all the images stored in the bucket."""
        blobs = self.storage_client.list_blobs(self.bucket_name)
        print("Images in the bucket:")
        for blob in blobs:
            print(blob.name)

    def download_from_bucket(self, source_blob_name, destination_file_name):
        """Downloads a file from the bucket."""
        # Get the blob object from the bucket
        blob = self.bucket.blob(source_blob_name)

        # Download the file to the specified local file path
        blob.download_to_filename(destination_file_name)
        print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")


if __name__ == "__main__":
    # Initialize the storage client with the path to your credentials file
    credentials_file = 'key.json'
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_file

    # Initialize the uploader with the bucket name
    bucket_name = 'bucket-get-started_argus2commsys'
    uploader = GoogleCloudUploader(bucket_name=bucket_name)

    # Path to your local image
    image_path = "testImg2.png"
    # Desired name of the file in the Cloud bucket
    destination_blob_name = os.path.basename(image_path)

    # Option 1: Use the class method to upload the file
    uploader.upload_image(image_path, destination_blob_name)

    # Option 2: Upload using the function and gs:// URI
    gs_uri = f"gs://{bucket_name}/{destination_blob_name}"
    uploader.upload_file_to_bucket(gs_uri, image_path)
    # List the images in the bucket (optional)
    uploader.list_images()
    local_store_path= 'LocalDatabase'
    local_data_name=f"{local_store_path}/{destination_blob_name}"
    uploader.download_from_bucket(destination_blob_name,local_data_name)
