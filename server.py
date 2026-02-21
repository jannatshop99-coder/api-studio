from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from rembg import remove

app = FastAPI()

# CORS Middleware (যাতে আপনার ওয়েবসাইট থেকে এপিআই কল করা যায়)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API is working properly on Render!"}

@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    try:
        # ছবি রিড করা এবং ব্যাকগ্রাউন্ড রিমুভ করা
        input_image = await file.read()
        output_image = remove(input_image)
        
        # পিএনজি (PNG) ফরম্যাটে ছবি রিটার্ন করা
        return Response(content=output_image, media_type="image/png")
    except Exception as e:
        return {"error": str(e)}