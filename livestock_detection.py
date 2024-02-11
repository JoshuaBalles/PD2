from ultralytics import YOLO

# Load a model
model = YOLO('model.pt')

# Run inference on an input source
model.predict(source=r'./input', conf=0.5, stream_buffer=True, save=True)
