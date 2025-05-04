import os

from dotenv import load_dotenv
from mistralai import Mistral


class HaikuService:
    def __init__(self, remote_source):
        self.remote_source = remote_source

    def _check(self, poem: list[str]) -> bool:
        return len(poem) == 3

    def _parse(self, remote_answer: str, delimiter: str) -> list[str]:
        result = []
        inside = False
        for line in remote_answer.split("\n"):
            if "#####" in line:
                if line.strip() != "#####":
                    result.append(line.replace("#####", "").strip())
                inside = not inside
                continue
            if inside:
                result.append(line.strip())
        return result

    def get(self) -> list[str]:
        answer = self.remote_source.get_remote_haiku()
        poem = self._parse(answer, "#####")
        if self._check(poem):
            return poem
        else:
            raise ValueError("Remote is not giving a good haiku")


class MistralHaikuSource:
    def __init__(self):
        if "MISTRAL_API_KEY" not in os.environ:
            load_dotenv()

        api_key = os.environ["MISTRAL_API_KEY"]
        self._model = "ministral-8b-latest"
        self._client = Mistral(api_key=api_key)

    def get_remote_haiku(self):
        prompt = """
            Write a haiku in english.
            In the answer the haiku should start with "#####" and end with "#####" in order to be easily parseable.
            The haiku should respect all conventionnal rules : a Japanese poem of seventeen syllables, in three lines of five, seven, and five, traditionally evoking images of the natural world.
            The poem should be about nature or computer science.
        """
        return self._get_answer(prompt)

    def _get_answer(self, prompt: str) -> str:
        chat_response = self._client.chat.complete(
            model=self._model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            timeout_ms=10000,
        )
        return chat_response.choices[0].message.content
