# run with: uvicorn main:app --reload
# oder lokal mit: python quiz.py

# https://www.youtube.com/watch?v=iFvCZD4iS2w&t=2s
# https://github.com/msoedov/langcorn/

# langcorn kreiert automatisch eine FastAPI aus einer langchain chain:

from langcorn import create_service

app = create_service(
    "quiz:chain"
)