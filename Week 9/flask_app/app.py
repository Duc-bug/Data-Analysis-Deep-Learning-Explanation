from pathlib import Path
from uuid import uuid4

import torch
import torch.nn as nn
from flask import Flask, render_template, request
from PIL import Image
from werkzeug.utils import secure_filename

APP_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = APP_DIR / "uploads"
WEIGHTS_PATH = APP_DIR.parent / "checkpoints" / "fmnist_mlp_weights.pth"

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
CLASS_NAMES = [
    "T-shirt_top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle_boot",
]


def build_model() -> nn.Module:
    return nn.Sequential(
        nn.Linear(28 * 28, 1000),
        nn.ReLU(),
        nn.Linear(1000, 10),
    )


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def preprocess_image(image_path: Path) -> torch.Tensor:
    image = Image.open(image_path).convert("L").resize((28, 28))
    x = torch.tensor(list(image.getdata()), dtype=torch.float32) / 255.0
    x = x.view(1, 28 * 28)
    return x


def predict(image_path: Path) -> tuple[str, list[tuple[str, float]]]:
    x = preprocess_image(image_path)
    with torch.no_grad():
        logits = MODEL(x)
        probs = torch.softmax(logits, dim=1)[0]
    topk = torch.topk(probs, k=3)
    top3 = [(CLASS_NAMES[i], float(probs[i] * 100)) for i in topk.indices.tolist()]
    return top3[0][0], top3


if not WEIGHTS_PATH.exists():
    raise FileNotFoundError(f"Model file not found: {WEIGHTS_PATH}")

MODEL = build_model()
MODEL.load_state_dict(torch.load(WEIGHTS_PATH, map_location="cpu"))
MODEL.eval()

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = str(UPLOAD_DIR)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    top3 = []
    error = None
    image_url = None

    if request.method == "POST":
        if "image" not in request.files:
            error = "Khong tim thay file anh trong form."
        else:
            file = request.files["image"]
            if file.filename == "":
                error = "Ban chua chon file."
            elif not allowed_file(file.filename):
                error = "Chi ho tro png, jpg, jpeg, webp."
            else:
                filename = secure_filename(file.filename)
                unique_name = f"{uuid4().hex}_{filename}"
                save_path = UPLOAD_DIR / unique_name
                file.save(save_path)
                prediction, top3 = predict(save_path)
                image_url = f"/uploads/{unique_name}"

    return render_template(
        "index.html",
        prediction=prediction,
        top3=top3,
        error=error,
        image_url=image_url,
    )


@app.route("/uploads/<path:filename>")
def uploaded_file(filename: str):
    from flask import send_from_directory

    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    app.run(debug=True)
