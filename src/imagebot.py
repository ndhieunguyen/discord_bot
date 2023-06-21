import replicate


class Imagebot:
    def __init__(self, token) -> None:
        self.api = replicate.Client(api_token=token)
        self.model = self.api.models.get("stability-ai/stable-diffusion")
        self.version = self.versions.get("db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf")

    def generate_image(self, query):
        output_url = self.version.predict(prompt=query)[0]
        return output_url
