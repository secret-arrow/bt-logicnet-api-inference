
import logging

from fastapi import FastAPI
import uvicorn
from protocol import MathQueryPayload
from starlette.responses import JSONResponse
from neuron import Neuron
import asyncio
lock = asyncio.Lock()


app = FastAPI()
neuron = Neuron()

@app.post("/math_query")
async def math_query(math_query_payload: MathQueryPayload):
    result = neuron.forward_request_to_subnet(math_query_payload)
    logging.info(f'Answer to user: {result}\n\n')
    return JSONResponse(
        content = {
            "ai_answer": result
        },
        status_code = 200
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
