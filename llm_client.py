import requests


class OllamaLLM:
    """
    Small Ollama client.
    - GET  /api/tags     -> list installed models
    - POST /api/generate -> generate answer
    """

    def __init__(self, base_url="http://localhost:11434", model="gemma3:4b"):
        self.base_url = base_url.rstrip("/")
        self.model = model

    def list_models(self) -> list[str]:
        r = requests.get(f"{self.base_url}/api/tags", timeout=8)
        r.raise_for_status()
        data = r.json()
        return [m.get("name") for m in data.get("models", []) if m.get("name")]

    def health_check(self) -> tuple[bool, str]:
        """
        Returns:
          (True, "OK...") if reachable + model exists
          (False, "Reason") otherwise
        """
        try:
            models = self.list_models()
            if not models:
                return False, "Ollama is running, but no models found. Run: ollama pull gemma3:4b"

            if self.model and self.model not in models:
                return False, f"Model '{self.model}' not found. Available: {', '.join(models[:6])}..."

            return True, "Connected and ready"
        except requests.exceptions.ConnectionError:
            return False, "Connection refused. Is Ollama running? Try: ollama serve"
        except requests.exceptions.Timeout:
            return False, "Timed out. Ollama might be busy — try again."
        except Exception as e:
            return False, str(e)

    def generate(self, prompt: str, temperature: float = 0.2, timeout: int = 120) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": float(temperature)},
        }

        r = requests.post(f"{self.base_url}/api/generate", json=payload, timeout=timeout)
        r.raise_for_status()
        data = r.json()
        return (data.get("response") or "").strip()
