from ultralytics import YOLO
model = YOLO('models/best.pt')
print(f"Model załadowany: {model}")
results = model.predict('input_videos/08fd33_4.mp4', device='cuda', save=True)
print(results[0])
for box in results[0].boxes:
    print(box)
