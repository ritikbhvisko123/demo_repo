# JobGPT - AI-Powered Job Search System

## 🚀 Project Overview

JobGPT is an intelligent AI-powered job search system built with Flask and Google's Gemini AI model. It provides two main functionalities:
1. **Job Search**: Find jobs based on user queries, skills, and location preferences
2. **Candidate Search**: Find suitable candidates based on specific requirements

The system uses natural language processing to understand user queries and automatically generates SQL queries to search through job and candidate databases.

## ✨ Key Features

- **AI-Powered Query Understanding**: Uses Google Gemini 1.5 Pro to interpret natural language job/candidate search queries
- **Intelligent SQL Generation**: Automatically converts user queries into optimized SQL statements
- **Dual Search Capabilities**: 
  - Job search with location-based filtering
  - Candidate search with skill and experience matching
- **JWT Authentication**: Secure user authentication and profile-based search
- **Smart Fallback**: Intelligent routing between different search strategies
- **Location Intelligence**: Understands city, state, and country-level location queries
- **Experience Matching**: Advanced experience level matching for both jobs and candidates
- **Query Validation**: Prevents SQL injection and malicious queries
- **Activity Tracking**: Logs user interactions for analytics

## 🏗️ Architecture

### Technology Stack
- **Backend**: Flask (Python web framework)
- **AI Model**: Google Gemini 1.5 Pro via LangChain
- **Database**: MySQL with custom connection management
- **Authentication**: JWT tokens
- **CORS**: Cross-origin resource sharing enabled

### Core Components

1. **Main Application (`final_new.py`)**
   - Flask web server
   - API endpoints for job and candidate search
   - AI query processing and routing

2. **Database Connection (`connect.py`)**
   - MySQL connection management
   - Query execution with security validation
   - Data insertion and tracking functions

3. **AI Processing Engine**
   - Query sentiment analysis
   - SQL query generation
   - Intelligent fallback mechanisms

## 🔌 API Endpoints

### 1. Job Search API
```
POST /find-job
```

**Request Body:**
```json
{
  "query": "Python developer with 3 years experience in Bangalore",
  "ip_address": "192.168.1.1",
  "user_id": "user123"
}
```

**Headers:**
```
Authorization: Bearer <jwt_token>
```

**Response:**
```json
{
  "status": true,
  "text": "Found matching jobs for Python developer",
  "prompt": "Python developer with 3 years experience in Bangalore",
  "job_message": "Found 5 jobs for you",
  "jobs": [...],
  "recommends": "Try searching for 'React developer' or 'Full stack developer'"
}
```

### 2. Candidate Search API
```
POST /find-user
```

**Request Body:**
```json
{
  "query": "Flutter developer with 2 years experience"
}
```

**Response:**
```json
{
  "status": true,
  "text": "Found matching candidates",
  "candidate_message": "Found 3 Candidates from database",
  "candidates": [...],
  "recommends": "Try searching for 'React Native developer' or 'Mobile app developer'",
  "query": "SELECT * FROM users WHERE..."
}
```

## 🗄️ Database Schema

### Jobs Table
- `job_id`, `job_title`, `job_description`, `job_responsibility`
- `job_key_skills`, `job_education`, `job_industry`
- `job_hiring_count`, `job_minimum_salary`, `job_maximum_salary`
- `job_salary_type`, `job_schedule`, `job_qualification`
- `job_ext_experience`, `job_created_at`, `company_id`

### Company Table
- `company_id`, `company_name`, `company_city`, `company_state`

### Users Table
- `user_id`, `user_profile`, `user_bio`, `user_skills`
- `user_experience`, `user_exp_years`, `user_exp_months`
- `user_total_exp_months`, `user_qualification`
- `user_city`, `user_state`, `user_created_at`

## 🧠 AI Processing Flow

### 1. Query Analysis
- User input is processed by Gemini AI
- System determines search intent (job vs. candidate)
- Location-based vs. skill-based search routing

### 2. SQL Generation
- AI generates optimized SQL queries based on user intent
- Queries include proper JOINs and WHERE clauses
- Location filtering (city/state level)
- Skill matching with OR conditions

### 3. Fallback Strategy
- If AI query generation fails, system falls back to profile-based search
- Uses JWT token data for user skills and experience
- Generates multiple targeted queries for comprehensive results

### 4. Result Processing
- Executes generated SQL queries
- Filters duplicate results
- Formats response with recommendations
- Tracks user activity

## 🔐 Security Features

- **SQL Injection Prevention**: Blocks dangerous SQL keywords
- **JWT Token Validation**: Secure user authentication
- **Input Sanitization**: Validates and cleans user inputs
- **Query Limiting**: Prevents excessive database queries
- **Error Handling**: Graceful error responses without exposing system details

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- MySQL database
- Google AI API key

### 1. Clone the Repository
```bash
git clone <repository-url>
cd job_ai_search
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file with your configuration:
```env
GOOGLE_API_KEY=your_google_ai_api_key
DB_HOST=your_database_host
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
```

### 4. Database Setup
Ensure your MySQL database has the required tables:
- `jobs` table with job-related fields
- `company` table with company information
- `users` table with candidate profiles
- `ai_job_gpt` table for tracking queries
- `activity_table` for activity logging

### 5. Run the Application
```bash
python final_new.py
```

The server will start on `http://0.0.0.0:5026`

## 📊 Usage Examples

### Job Search Queries
- "Python developer in Mumbai"
- "Frontend developer with React experience"
- "Data scientist with 5 years experience"
- "Remote work opportunities in IT"
- "High salary jobs in Bangalore"

### Candidate Search Queries
- "Flutter developer with 2 years experience"
- "Sales executive in Delhi"
- "Marketing manager with MBA"
- "Python developer with Django skills"

## 🔧 Configuration

### AI Model Settings
- **Model**: `gemini-1.5-pro-latest`
- **Temperature**: 0.7 (job search), 0.5 (query routing)
- **Max Results**: 10 for jobs, 5 for candidates

### Database Settings
- **Connection Pool**: Automatic connection management
- **Query Timeout**: Built-in error handling
- **Result Limiting**: Configurable result limits

## 📈 Performance Features

- **Query Optimization**: AI-generated optimized SQL queries
- **Result Deduplication**: Prevents duplicate job/candidate listings
- **Intelligent Caching**: Connection pooling for database operations
- **Async Processing**: Non-blocking query execution

## 🐛 Error Handling

The system includes comprehensive error handling:
- **AI Model Errors**: Graceful fallback to profile-based search
- **Database Errors**: Connection retry and error logging
- **Query Errors**: Validation and sanitization
- **Authentication Errors**: Clear error messages for invalid tokens

## 🔍 Monitoring & Analytics

- **Query Tracking**: Logs all user search queries
- **Activity Monitoring**: Tracks user interactions
- **Performance Metrics**: Query execution time monitoring
- **Error Logging**: Comprehensive error tracking

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is proprietary software developed by Remark HR.

## 🆘 Support

For technical support or questions:
- Check the API documentation
- Review error logs
- Contact the development team

## 🔮 Future Enhancements

- **Multi-language Support**: Support for regional languages
- **Advanced Filtering**: More sophisticated search algorithms
- **Machine Learning**: Improved query understanding over time
- **Real-time Updates**: Live job/candidate updates
- **Mobile App**: Native mobile application
- **Analytics Dashboard**: Advanced reporting and insights

---

**Built with ❤️ by Remark HR Team** 
