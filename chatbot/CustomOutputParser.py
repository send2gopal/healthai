from llama_index.core.output_parsers import ChainableOutputParser
from documentSchema import Education

class CustomAlbumOutputParser(ChainableOutputParser):
    """Custom Album output parser.

    Assume first line is name and artist.

    Assume each subsequent line is the song.

    """

    def __init__(self, verbose: bool = True):
        self.verbose = verbose

    def parse(self, output: str) -> Education:
        """Parse output."""
        if self.verbose:
            print(f"> Raw output: {output}")
        lines = output.split("\n")
        name, artist = lines[0].split(",")
        return Education()