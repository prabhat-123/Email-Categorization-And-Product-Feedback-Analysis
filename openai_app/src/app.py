import uvicorn
from fastapi import FastAPI, Request
from product_sentiment_analyzer import ProductSentimentAnalyzer

app = FastAPI()

@app.post("/analyze_product_sentiment")  
async def analyze_product_sentiment(request: Request):  
    form_data = await request.form()
    query = form_data.get("query")
    sentiment_analyzer = ProductSentimentAnalyzer()  
    sentiment_response = sentiment_analyzer.analyze_product_query(query) 
    return sentiment_response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


# uvicorn app:app --reload --host 0.0.0.0 --port 8000
