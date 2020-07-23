
from fastapi import FastAPI
import uvicorn
from protocol import MathQueryPayload
from starlette.responses import JSONResponse
from neuron import Neuron
import bittensor as bt


app = FastAPI()
neuron = Neuron()

@app.post("/math_query")
async def math_query(math_query_payload: MathQueryPayload):
    # Await the result from the neuron
    results = await neuron.forward_request_to_subnet(math_query_payload)
    result = results[0]

    # Extracting the data from the LogicSynapse result
    if result:
        logic_question = result.logic_question
        ai_answer = result.logic_answer
        reasoning = result.logic_reasoning

        # Log detailed information
        bt.logging.info(f"Logic Question: {logic_question}")
        bt.logging.info(f"AI Answer: {ai_answer}")
        bt.logging.info(f"Reasoning: {reasoning}")

        # Return JSON response with all relevant fields
        return JSONResponse(
            content={
                "logic_question": logic_question,
                "ai_answer": ai_answer,
                "reasoning": reasoning,
            },
            status_code=200
        )
    else:
        # Handle cases where no result is returned
        return JSONResponse(
            content={"error": "No response from neuron"},
            status_code=500
        )

@app.get("/status")
async def status():
    return JSONResponse(content={"status": "ok"}, status_code=200)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8088)
