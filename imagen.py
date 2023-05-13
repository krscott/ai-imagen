# pyright: reportUnknownMemberType=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownArgumentType = false
# pyright: reportMissingTypeStubs=false

from typing import Any
from dotenv import load_dotenv
from transformers import OpenAiAgent
import os
import sys


def main():
    _ = load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    assert api_key

    agent = OpenAiAgent(model="text-davinci-003", api_key=api_key)

    for filepath in sys.argv[1:]:
        # Assert file does not exist
        assert not os.path.exists(filepath)

        filename = os.path.split(filepath)[-1]
        print("Generating", filename)

        # Assert file extension is valid
        assert os.path.splitext(filename)[-1].lower() in [".jpg", ".jpeg", ".png"]

        # Generate an image
        image: Any = agent.run(
            "Generate an image `filename`",
            remote=True,
            filename=filename,
        )

        image.save(filepath)


if __name__ == "__main__":
    main()
