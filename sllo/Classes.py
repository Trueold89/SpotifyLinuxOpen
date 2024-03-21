from enum import Enum


class SpotifyLink:
    class SMTH(Enum):
        CTYPE = 0
        CID = 1

    def __init__(self, link: str) -> None:
        """
        :rtype: None
        """
        if not ("open.spotify.com" in link):
            raise ValueError("This is not a SpotifyOpen link")
        self.__link = link

    def __getsmth(self, item: SMTH) -> str:
        """
        :type item: SMTH
        :rtype: str
        """
        split = self.__link[8:].split("/")[1:]
        return split[item.value]

    def __gettype(self) -> str:
        """
        :return: Content type
        :rtype: str
        """
        return self.__getsmth(self.SMTH.CTYPE)

    def __getid(self) -> str:
        return self.__getsmth(self.SMTH.CID)

    def uri(self):
        ctype = self.__gettype()
        cid = self.__getid()
        return f"spotify:{ctype}:{cid}"
