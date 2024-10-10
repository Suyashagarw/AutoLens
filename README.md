
# AutoLens

## Application Description

AutoLens is a smart photo album, built using AWS services, provides users with a highly scalable, reliable, and secure platform for managing photos. The application uses AI to automatically sort photos into albums based on image content. Key features include image recognition, search capabilities, and caching for an enhanced user experience.

### Key Components:
1. **Image Upload & Categorization**: Users can upload images, which are stored in S3 and analyzed by AWS Rekognition. Generated labels are stored in DynamoDB along with image metadata.
2. **Search Functionality**: Users can search for images via labels, categories, or keywords, with fast access through Redis and OpenSearch.
3. **Efficient Image Processing**: Redis cache is used to reduce processing time during searches, improving performance.

## Application Architecture

The application’s backend relies on a set of AWS services to manage photo uploads, processing, and retrieval. Below is a summary of the architecture:

- **Upload Flow**: Users upload images, which are stored in S3. The images are processed by AWS Rekognition for label generation. These labels, along with image metadata, are stored in DynamoDB and Redis.
- **Search Flow**: Users initiate search requests via keywords or labels. These requests are processed through OpenSearch and results are retrieved from the Redis cache for faster performance.

### Advanced Features:
- **SQS Queuing**: Used for faster response times during image uploads and searches.
- **Redis Caching**: Used to store image URLs for faster access during searches.
- **OpenSearch Integration**: Enhances search functionality for easier image retrieval.
- **CloudWatch Monitoring**: Integrated for monitoring the health and performance of the system.

