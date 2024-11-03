import typing


class AffineCipher:
    """
    This class implements Affine Cipher.
    """

    def __init__(self, key_1: str, key_2: str, alphabet: typing.List[str]) -> None:
        self.key_1 = key_1
        self.key_2 = key_2
        self.alphabet = alphabet

    def _encrypt_letter(self, letter: str) -> str:
        x = self.alphabet.find(letter)
        encr_letter_index = (self.key_1 * x + self.key_2) % len(self.alphabet)
        encr_letter = self.alphabet[encr_letter_index]

        return encr_letter

    def encrypt(self, sentence: str) -> str:
        sentence = sentence.lower()
        encr_sentence = ""

        for letter in sentence:
            encr_sentence += (
                self._encrypt_letter(letter) if letter in self.alphabet else ""
            )

        return encr_sentence
