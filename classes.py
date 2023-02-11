class Auto:
    def __init__(self, merkki, malli, rekisterinumero):
        self.merkki = merkki
        self.malli = malli
        self.rekisterinumero = rekisterinumero

    def __str__(self):
        return f'{self.merkki} {self.malli} ({self.rekisterinumero})'

# Tehtävän anto oli tehdä samaan mutta nyt classes ja auto on erikseen 
# koska nii kannattaa oikeasti tehdä jotta classes on siistimpi
