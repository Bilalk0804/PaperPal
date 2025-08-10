# LLM-Powered Intelligent Query–Retrieval System

A sophisticated document processing and query system designed for insurance, legal, HR, and compliance domains. This system uses Retrieval-Augmented Generation (RAG) to provide accurate, contextual responses based on document content.

## 🚀 Features

### Core Capabilities
- **Multi-format Document Processing**: PDF, DOCX, and email files
- **Semantic Search**: FAISS-based vector search with sentence transformers
- **Structured Outputs**: JSON responses with confidence scores and reasoning
- **Domain Classification**: Automatic classification (insurance, legal, HR, compliance)
- **Explainable AI**: Detailed reasoning for all responses
- **Batch Processing**: Handle multiple queries efficiently

### Technical Features
- **Vector Database**: FAISS for fast similarity search
- **Embeddings**: Sentence transformers for semantic understanding
- **LLM Integration**: Ollama with local model support
- **REST API**: FastAPI server with comprehensive endpoints
- **Structured Responses**: Pydantic models for consistent output

## 🏗️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Document      │    │   Vector        │    │   LLM           │
│   Processor     │───▶│   Store         │───▶│   Generator     │
│                 │    │   (FAISS)       │    │   (Ollama)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   PDF/DOCX/     │    │   Semantic      │    │   Structured    │
│   Email Parser  │    │   Search        │    │   JSON Output   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📋 Requirements

### System Requirements
- Python 3.8+
- 8GB+ RAM (for large document processing)
- Ollama installed and running locally

### Python Dependencies
See `requirements.txt` for complete list:
- `langchain` & `langchain-ollama`
- `faiss-cpu` for vector search
- `sentence-transformers` for embeddings
- `PyPDF2` & `python-docx` for document processing
- `fastapi` & `uvicorn` for API server

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd intelligent-query-system
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Ollama and download model**
   ```bash
   # Install Ollama (https://ollama.ai)
   ollama pull deepseek-r1:latest
   ```

## 🚀 Quick Start

### 1. Run the Demo
```bash
python demo.py
```
This will:
- Create sample documents (insurance, employment, compliance)
- Process and index them
- Run example queries
- Show system capabilities

### 2. Start the API Server
```bash
python api_server.py
```
Access the API at:
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### 3. Use the System Programmatically
```python
from rag_system import IntelligentQuerySystem

# Initialize system
system = IntelligentQuerySystem()

# Add documents
system.add_documents("path/to/your/documents")

# Query the system
response = system.query("What is the coverage limit?")
print(response.answer)
print(response.confidence)
```

## 📚 Usage Examples

### Document Processing
```python
from document_processor import DocumentProcessor

processor = DocumentProcessor(chunk_size=1500, chunk_overlap=300)
chunks = processor.process_directory("documents/")
```

### Vector Search
```python
from vector_store import VectorStore

store = VectorStore()
store.add_documents(chunks)
results = store.semantic_search("insurance coverage", k=5)
```

### API Usage
```bash
# Upload documents
curl -X POST "http://localhost:8000/upload" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "files=@document1.pdf" \
  -F "files=@document2.docx"

# Query the system
curl -X POST "http://localhost:8000/query" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the coverage limit?", "top_k": 5}'
```

## 🔧 Configuration

### System Parameters
- **Chunk Size**: Default 1500 tokens (adjustable in `DocumentProcessor`)
- **Chunk Overlap**: Default 300 tokens for context continuity
- **Search Threshold**: Default 0.3 similarity score
- **Top-K Results**: Default 5 documents per query

### Model Configuration
- **Embedding Model**: `all-MiniLM-L6-v2` (384 dimensions)
- **LLM Model**: `deepseek-r1:latest` (via Ollama)
- **Vector Index**: FAISS Inner Product (IP) index

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information and endpoints |
| `/health` | GET | System health check |
| `/upload` | POST | Upload and process documents |
| `/query` | POST | Process single query |
| `/batch-query` | POST | Process multiple queries |
| `/stats` | GET | System statistics |
| `/save` | POST | Save system state |
| `/load` | POST | Load system state |

## 🎯 Domain-Specific Features

### Insurance Domain
- Policy coverage analysis
- Claims process information
- Premium and deductible details
- Exclusions and limitations

### Legal Domain
- Contract clause extraction
- Compliance requirements
- Legal obligations
- Termination conditions

### HR Domain
- Employment terms
- Benefits and compensation
- Workplace policies
- Training requirements

### Compliance Domain
- Regulatory requirements
- Data protection rules
- Safety standards
- Penalty structures

## 🔍 Query Examples

### Insurance Queries
```
"What is the property coverage limit?"
"What is the claims process?"
"What are the policy exclusions?"
```

### Legal Queries
```
"What are the termination conditions?"
"What are the non-compete restrictions?"
"What confidentiality obligations exist?"
```

### HR Queries
```
"What is the bonus structure?"
"What benefits are provided?"
"What is the work schedule?"
```

### Compliance Queries
```
"What data protection requirements exist?"
"What safety training is required?"
"What are the penalty structures?"
```

## 📈 Performance Optimization

### For Large Document Collections
1. **Increase chunk size** for better context
2. **Adjust overlap** for better continuity
3. **Use GPU acceleration** for embeddings
4. **Implement caching** for frequent queries

### For Real-time Applications
1. **Pre-index documents** during off-peak hours
2. **Use batch processing** for multiple queries
3. **Implement connection pooling** for database
4. **Add response caching** for similar queries

## 🛡️ Security Considerations

- **Document Encryption**: Implement at-rest encryption
- **Access Control**: Add authentication/authorization
- **Data Privacy**: Implement data retention policies
- **Audit Logging**: Track all queries and responses

## 🔧 Troubleshooting

### Common Issues

1. **Ollama not running**
   ```bash
   ollama serve
   ```

2. **Memory issues with large documents**
   - Reduce chunk size
   - Process documents in batches
   - Increase system RAM

3. **Slow search performance**
   - Use GPU for embeddings
   - Optimize FAISS index
   - Reduce search threshold

### Debug Mode
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Check the API documentation at `/docs`
- Review the demo script for examples

---

**Built with ❤️ for intelligent document processing and query systems**
