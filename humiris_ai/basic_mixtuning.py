import requests

class MessageType:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

class BasicPayload:
    def __init__(self, mix_tuning_id: str, messages: list, temperature: float, max_tokens: int):
        self.mix_tuning_id = mix_tuning_id
        self.messages = messages
        self.temperature = temperature
        self.max_tokens = max_tokens

class BasicMoAi:
    def __init__(self, api_key: str):
        self.api_url = 'https://moai-service-app.humiris.ai/api/api-key-operators/use-basic-mixtuning'
        self.api_key = api_key

    def use_basic_mixtuning(self, payload: BasicPayload):
        headers = {
            'moai-api-key': self.api_key,
            'Content-Type': 'application/json'
        }

         # Convert payload and MessageType objects to dictionaries
        payload_dict = {
            "mix_tuning_id": payload.mix_tuning_id,
            "messages": [{"role": msg.role, "content": msg.content} for msg in payload.messages],
            "temperature": payload.temperature,
            "max_tokens": payload.max_tokens
        }

        try:
            response = requests.post(self.api_url, json=vars(payload_dict), headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            raise Exception(f"Failed to send request: {error}")

