```python
from fastapi import FastAPI
from hello_world import HelloWorld

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # Initialize HelloWorld with your API key
    global hw
    hw = HelloWorld("your_api_key")

@app.get("/hello_world")
async def hello_world():
    try:
        # Call the hello_world method
        message = hw.hello_world()
        return {"message": message}
    except Exception as e:
        return {"error": str(e)}
```
