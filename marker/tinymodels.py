from marker.postprocessors.editor import load_editing_model
from surya.model.detection import segformer
from texify.model.model import load_model as load_texify_model
from texify.model.processor import load_processor as load_texify_processor
from marker.settings import settings
from surya.model.recognition.model import load_model as load_recognition_model
from surya.model.recognition.processor import load_processor as load_recognition_processor
from surya.model.ordering.model import load_model as load_order_model
from surya.model.ordering.processor import load_processor as load_order_processor

from marker.ocr.lang import replace_langs_with_codes, validate_langs
from marker.settings import settings

def setup_recognition_model(langs=None, device=None, dtype=None):
    if device:
        rec_model = load_recognition_model(langs=langs, device=device, dtype=dtype)
    else:
        rec_model = load_recognition_model(langs=langs)
    rec_processor = load_recognition_processor()
    rec_model.processor = rec_processor
    return rec_model


def setup_detection_model(device=None, dtype=None):
    if device:
        model = segformer.load_model(device=device, dtype=dtype)
    else:
        model = segformer.load_model()

    processor = segformer.load_processor()
    model.processor = processor
    return model


def setup_texify_model(device=None, dtype=None):
    if device:
        texify_model = load_texify_model(checkpoint=settings.TEXIFY_MODEL_NAME, device=device, dtype=dtype)
    else:
        texify_model = load_texify_model(checkpoint=settings.TEXIFY_MODEL_NAME, device=settings.TORCH_DEVICE_MODEL, dtype=settings.TEXIFY_DTYPE)
    texify_processor = load_texify_processor()
    texify_model.processor = texify_processor
    return texify_model


def setup_layout_model(device=None, dtype=None):
    if device:
        model = segformer.load_model(checkpoint=settings.LAYOUT_MODEL_CHECKPOINT, device=device, dtype=dtype)
    else:
        model = segformer.load_model(checkpoint=settings.LAYOUT_MODEL_CHECKPOINT)
    processor = segformer.load_processor(checkpoint=settings.LAYOUT_MODEL_CHECKPOINT)
    model.processor = processor
    return model


def setup_order_model(device=None, dtype=None):
    if device:
        model = load_order_model(device=device, dtype=dtype)
    else:
        model = load_order_model()
    processor = load_order_processor()
    model.processor = processor
    return model