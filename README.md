# ai-imagen

Create new images based on the given filenames.

A minimal usage example of [HuggingFace Transformers Agent](https://huggingface.co/docs/transformers/transformers_agents).

## Usage

Copy `.env.example` and rename to `.env`.

Add your OpenAI API key.

Run the script:
```
python imagen.py filename1 [filename2 ...]
```

## Example

```
python imagen.py corgi-in-space.png
```

Output:

![corgi-in-space.png](docs/corgi-in-space.png)
