"""
FastAPI Demo Server
Perfect for demonstrating Python API integration with n8n workflows

This server provides several endpoints that can be called from n8n:
- Text processing and analysis
- Data transformation
- File processing
- Machine learning predictions

Run with: uvicorn fastapi_demo:app --host 0.0.0.0 --port 8003
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import json
import re
from datetime import datetime
import hashlib

# Initialize FastAPI app
app = FastAPI(
    title="Python Meetup Demo API",
    description="Demo API for n8n integration and Python workflow automation",
    version="1.0.0",
)

# Enable CORS for n8n integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic models for request/response
class TextRequest(BaseModel):
    text: str
    options: Dict[str, Any] = {}


class TextResponse(BaseModel):
    original_text: str
    processed_text: str
    metadata: Dict[str, Any]


class FileRequest(BaseModel):
    filename: str
    content: str
    file_type: str


class AnalysisResponse(BaseModel):
    analysis: Dict[str, Any]
    timestamp: str


@app.get("/")
async def root():
    """Root endpoint - API information"""
    return {
        "message": "Python Meetup Demo API",
        "version": "1.0.0",
        "endpoints": [
            "/process-text",
            "/analyze-sentiment",
            "/extract-entities",
            "/process-file",
            "/transform-data",
            "/health",
        ],
        "description": "Demo API for n8n workflow integration",
        "timestamp": datetime.now().isoformat(),
    }


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "uptime": "running",
        "service": "python-demo-api",
    }


@app.post("/process-text", response_model=TextResponse)
async def process_text(request: TextRequest):
    """
    Process text with various options

    Example n8n workflow:
    1. Manual trigger → Text input → This endpoint → Response processing
    """
    try:
        text = request.text
        options = request.options

        # Text processing operations
        processed_text = text

        # Convert to lowercase if requested
        if options.get("lowercase", False):
            processed_text = processed_text.lower()

        # Remove extra whitespace
        if options.get("clean_whitespace", True):
            processed_text = re.sub(r"\s+", " ", processed_text).strip()

        # Remove special characters
        if options.get("remove_special_chars", False):
            processed_text = re.sub(r"[^\w\s]", "", processed_text)

        # Generate metadata
        metadata = {
            "original_length": len(text),
            "processed_length": len(processed_text),
            "word_count": len(processed_text.split()),
            "char_count": len(processed_text),
            "processing_options": options,
            "processing_timestamp": datetime.now().isoformat(),
            "text_hash": hashlib.md5(text.encode()).hexdigest()[:8],
        }

        return TextResponse(
            original_text=text, processed_text=processed_text, metadata=metadata
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Text processing failed: {str(e)}")


@app.post("/analyze-sentiment", response_model=AnalysisResponse)
async def analyze_sentiment(request: TextRequest):
    """
    Simple sentiment analysis demo
    In production, use libraries like TextBlob, VADER, or transformers
    """
    try:
        text = request.text.lower()

        # Simple keyword-based sentiment (for demo purposes)
        positive_words = [
            "good",
            "great",
            "excellent",
            "amazing",
            "wonderful",
            "fantastic",
            "love",
            "best",
            "awesome",
        ]
        negative_words = [
            "bad",
            "terrible",
            "awful",
            "horrible",
            "hate",
            "worst",
            "disgusting",
            "poor",
        ]

        positive_count = sum(1 for word in positive_words if word in text)
        negative_count = sum(1 for word in negative_words if word in text)

        # Calculate sentiment score
        total_sentiment_words = positive_count + negative_count
        if total_sentiment_words == 0:
            sentiment = "neutral"
            score = 0.0
        else:
            score = (positive_count - negative_count) / total_sentiment_words
            if score > 0.1:
                sentiment = "positive"
            elif score < -0.1:
                sentiment = "negative"
            else:
                sentiment = "neutral"

        analysis = {
            "sentiment": sentiment,
            "score": round(score, 3),
            "positive_words": positive_count,
            "negative_words": negative_count,
            "confidence": min(abs(score) + 0.5, 1.0),
            "text_length": len(text),
            "word_count": len(text.split()),
        }

        return AnalysisResponse(analysis=analysis, timestamp=datetime.now().isoformat())

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Sentiment analysis failed: {str(e)}"
        )


@app.post("/extract-entities", response_model=AnalysisResponse)
async def extract_entities(request: TextRequest):
    """
    Simple entity extraction demo
    Extracts emails, phone numbers, URLs, and potential names

    In production, use spaCy, NLTK, or transformers for better results
    """
    try:
        text = request.text

        # Email regex pattern
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        emails = re.findall(email_pattern, text)

        # Phone number pattern (simplified)
        phone_pattern = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
        phones = re.findall(phone_pattern, text)

        # URL pattern
        url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        urls = re.findall(url_pattern, text)

        # Simple capital word extraction (potential proper nouns)
        capital_words = re.findall(r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b", text)

        analysis = {
            "emails": emails,
            "phone_numbers": phones,
            "urls": urls,
            "potential_names": capital_words,
            "entity_counts": {
                "emails": len(emails),
                "phones": len(phones),
                "urls": len(urls),
                "names": len(capital_words),
            },
            "text_length": len(text),
        }

        return AnalysisResponse(analysis=analysis, timestamp=datetime.now().isoformat())

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Entity extraction failed: {str(e)}"
        )


@app.post("/process-file", response_model=AnalysisResponse)
async def process_file(request: FileRequest):
    """
    File processing demo - analyzes file content
    Demonstrates how to handle different file types
    """
    try:
        filename = request.filename
        content = request.content
        file_type = request.file_type

        # Basic file analysis
        analysis = {
            "filename": filename,
            "file_type": file_type,
            "size": len(content.encode("utf-8")),
            "line_count": len(content.splitlines()),
            "word_count": len(content.split()),
            "char_count": len(content),
            "file_extension": filename.split(".")[-1] if "." in filename else "unknown",
        }

        # Type-specific processing
        if file_type == "text" or filename.endswith(".txt"):
            # Text file specific analysis
            sentences = content.split(".")
            analysis["sentence_count"] = len(sentences)
            analysis["avg_words_per_sentence"] = len(content.split()) / max(
                len(sentences), 1
            )

        elif file_type == "json" or filename.endswith(".json"):
            # JSON file analysis
            try:
                json_data = json.loads(content)
                analysis["json_structure"] = {
                    "type": type(json_data).__name__,
                    "keys": list(json_data.keys())
                    if isinstance(json_data, dict)
                    else [],
                    "is_valid_json": True,
                }
            except:
                analysis["json_structure"] = {"is_valid_json": False}

        elif file_type == "csv" or filename.endswith(".csv"):
            # CSV file analysis
            lines = content.splitlines()
            if len(lines) > 1:
                analysis["csv_structure"] = {
                    "header": lines[0].split(","),
                    "row_count": len(lines) - 1,
                    "column_count": len(lines[0].split(",")) if lines[0] else 0,
                }

        return AnalysisResponse(analysis=analysis, timestamp=datetime.now().isoformat())

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File processing failed: {str(e)}")


@app.post("/transform-data")
async def transform_data(request: Dict[str, Any]):
    """
    Generic data transformation endpoint
    Perfect for n8n data processing workflows
    """
    try:
        data = request.get("data", [])
        transformations = request.get("transformations", [])

        transformed_data = data

        # Apply transformations
        for transform in transformations:
            transform_type = transform.get("type")

            if transform_type == "filter":
                # Filter data based on condition
                field = transform.get("field")
                value = transform.get("value")
                operator = transform.get("operator", "equals")

                if operator == "equals":
                    transformed_data = [
                        item for item in transformed_data if item.get(field) == value
                    ]
                elif operator == "contains":
                    transformed_data = [
                        item
                        for item in transformed_data
                        if value in str(item.get(field, ""))
                    ]

            elif transform_type == "map":
                # Map/transform fields
                field = transform.get("field")
                new_field = transform.get("new_field", field)
                function = transform.get("function", "identity")

                for item in transformed_data:
                    original_value = item.get(field)
                    if function == "uppercase":
                        item[new_field] = str(original_value).upper()
                    elif function == "lowercase":
                        item[new_field] = str(original_value).lower()
                    elif function == "length":
                        item[new_field] = len(str(original_value))
                    else:
                        item[new_field] = original_value

            elif transform_type == "sort":
                # Sort data
                field = transform.get("field")
                reverse = transform.get("reverse", False)
                transformed_data.sort(key=lambda x: x.get(field, ""), reverse=reverse)

        return {
            "original_count": len(data),
            "transformed_count": len(transformed_data),
            "transformations_applied": len(transformations),
            "data": transformed_data,
            "timestamp": datetime.now().isoformat(),
        }

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Data transformation failed: {str(e)}"
        )


@app.get("/metrics-demo")
async def metrics_demo():
    """
    Demo endpoint showing metrics that could be sent to Prometheus
    """
    import random
    import time

    # Simulate some metrics
    metrics = {
        "requests_total": random.randint(100, 1000),
        "response_time_ms": random.uniform(50, 500),
        "active_connections": random.randint(5, 50),
        "memory_usage_mb": random.uniform(100, 500),
        "cpu_usage_percent": random.uniform(10, 80),
        "error_rate": random.uniform(0, 5),
        "timestamp": time.time(),
    }

    return metrics


if __name__ == "__main__":
    import uvicorn

    print("Starting FastAPI demo server...")
    print("Available endpoints:")
    print("- GET  /")
    print("- GET  /health")
    print("- POST /process-text")
    print("- POST /analyze-sentiment")
    print("- POST /extract-entities")
    print("- POST /process-file")
    print("- POST /transform-data")
    print("- GET  /metrics-demo")
    print("\nServer will be available at: http://localhost:8003")

    uvicorn.run(app, host="0.0.0.0", port=8003)
