# Serverless Image Processing Pipeline

A serverless image processing pipeline built using **AWS S3, AWS Lambda, IAM, and Amazon CloudWatch**.

## Project Overview

This project automatically processes images whenever a new image is uploaded to an Amazon S3 bucket.

The workflow is:

1. An image is uploaded to the **Input S3 Bucket**.
2. S3 automatically triggers an **AWS Lambda function** through an S3 event notification.
3. Lambda retrieves and processes the image using **Python and Pillow**.
4. The image is resized and stored in a separate **Output S3 Bucket**.
5. Lambda execution details and application logs are captured in **Amazon CloudWatch Logs**.

## Architecture

```text
                Upload Image
                     │
                     ▼
             ┌─────────────────┐
             │   S3 Input      │
             │     Bucket      │
             └────────┬────────┘
                      │
                S3 Event
                Notification
                      │
                      ▼
             ┌─────────────────┐
             │  AWS Lambda     │
             │ Python + Pillow │
             └────────┬────────┘
                      │
                Resize Image
                      │
                      ▼
             ┌─────────────────┐
             │   S3 Output     │
             │     Bucket      │
             └─────────────────┘

                      │
                      ▼
             ┌─────────────────┐
             │  CloudWatch     │
             │      Logs       │
             └─────────────────┘
```

## AWS Services Used

* **Amazon S3** – Stores input and processed images.
* **AWS Lambda** – Processes images automatically without managing servers.
* **AWS IAM** – Provides Lambda with controlled access to S3.
* **Amazon CloudWatch** – Monitors Lambda executions and stores application logs.

## Technologies

* Python
* Pillow
* AWS Lambda
* Amazon S3
* AWS IAM
* Amazon CloudWatch
* Serverless Architecture

## Key Features

* Event-driven image processing
* Automatic Lambda invocation
* Image resizing using Pillow
* Separate input and output S3 buckets
* IAM-based access control
* CloudWatch logging and monitoring
* No server management

## Project Flow

```text
Image Upload
     ↓
S3 Input Bucket
     ↓
S3 Event Notification
     ↓
Lambda Function
     ↓
Pillow Image Processing
     ↓
Resize Image
     ↓
S3 Output Bucket
     ↓
CloudWatch Logs
```

## Learning Outcomes

Through this project, I gained hands-on experience with:

* Building serverless applications on AWS
* Implementing event-driven architectures
* Configuring S3 → Lambda integration
* Working with AWS IAM permissions
* Using Lambda Layers for Python dependencies
* Processing files using Python
* Monitoring Lambda functions using CloudWatch
