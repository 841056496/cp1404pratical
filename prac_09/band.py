class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musician_strs = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strs)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician in the band playing their instrument."""
        return '\n'.join([musician.play() for musician in self.musicians])
