import io
import torch
from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
import uvicorn
from contextlib import asynccontextmanager 

from my_model_definition import ImageClassifier, transform_image_for_prediction, device

MODEL_PATH = "model.pth" 

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Đang tải mô hình từ: {MODEL_PATH}")
    print(f"Sử dụng device: {device}")
    try:
        model_instance = ImageClassifier()
        
        model_instance.load_state_dict(torch.load(MODEL_PATH, map_location=device))
        
        model_instance.eval()
        
        app.state.model = model_instance.to(device)
        
        print("Mô hình đã được tải thành công và sẵn sàng cho dự đoán.")
    except FileNotFoundError:
        app.state.model = None 
        print(f"Lỗi: Không tìm thấy file mô hình tại '{MODEL_PATH}'. API sẽ không hoạt động chính xác.")
    except Exception as e:
        app.state.model = None
        print(f"Lỗi nghiêm trọng khi tải mô hình: {e}")
    
    yield

    print("Ứng dụng đang tắt...")
    if hasattr(app.state, 'model') and app.state.model is not None:
        del app.state.model 
        print("Model đã được dọn dẹp.")


app = FastAPI(title="Image Classification API", version="1.0.0", lifespan=lifespan)


@app.get("/", summary="Endpoint gốc", description="Trả về thông điệp chào mừng.")
def read_root():
    if not hasattr(app.state, 'model') or app.state.model is None:
        return {"message": "Chào mừng bạn đến với API! LƯU Ý: Mô hình chưa được tải thành công, kiểm tra logs."}
    return {"message": "Chào mừng bạn đến với API phục vụ mô hình phân loại ảnh!"}

@app.post("/predict/", summary="Dự đoán lớp của ảnh", description="Tải lên một ảnh và nhận về lớp dự đoán cùng xác suất.")
async def predict_image(file: UploadFile = File(..., description="File ảnh cần phân loại.")):

    if not hasattr(app.state, 'model') or app.state.model is None:
        raise HTTPException(status_code=503, detail="Mô hình chưa sẵn sàng hoặc tải thất bại. Vui lòng kiểm tra logs server.")
    
    current_model = app.state.model 

    try:
        image_bytes = await file.read()
        input_tensor = transform_image_for_prediction(image_bytes)
        input_tensor = input_tensor.to(device)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Lỗi xử lý ảnh: {str(ve)}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Lỗi tiền xử lý ảnh: {str(e)}")

    try:
        with torch.no_grad():
            output_logits = current_model(input_tensor) 

        probabilities = torch.softmax(output_logits[0], dim=0)
        predicted_score, predicted_idx = torch.max(probabilities, 0)

        class_names = {0: "Class 0", 1: "Class 1"}
        predicted_class_name = class_names.get(predicted_idx.item(), "Không xác định")

        return {
            "filename": file.filename,
            "predicted_class_index": predicted_idx.item(),
            "predicted_class_name": predicted_class_name,
            "confidence_score": predicted_score.item(),
            "all_class_probabilities": probabilities.tolist()
        }
    except Exception as e:
        print(f"Lỗi trong quá trình dự đoán: {e}")
        raise HTTPException(status_code=500, detail=f"Lỗi máy chủ nội bộ trong quá trình dự đoán: {str(e)}")
