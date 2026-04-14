import re
from .base_masker import BaseMasker

class SimpleMasker(BaseMasker):
    def mask(self, text: str) -> dict:
        detected = []

        def replace(pattern, tag, text):
            matches = re.findall(pattern, text)
            for m in matches:
                detected.append({
                    "type": tag,
                    "original": m,
                    "masked": f"[{tag}]"
                })
                text = text.replace(m, f"[{tag}]")
            return text

        text = replace(r'[\w\.-]+@[\w\.-]+', "EMAIL", text)
        text = replace(r'\b\+?\d{7,15}\b', "PHONE", text)
        text = replace(r'\b\d{11}\b', "ID", text)

        return {
            "masked_text": text,
            "detected_pii": detected
        }