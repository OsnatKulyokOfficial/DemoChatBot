from fastapi import FastAPI, Request, Response
import uvicorn
app = FastAPI()

# Here you can do things such as load your models

@app.get("/api/v1/inference")
def read_root(input_text: str):
    return f"Hello {input_text}!"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8085)