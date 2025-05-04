from main.service import HaikuService


class TestHaikuService:
    def test_get_haiku(self, haiku_service: HaikuService):
        poem = haiku_service.get()
        assert len(poem) == 3

    def test_check_haiku_length_validate_length_3(self, haiku_service: HaikuService):
        assert haiku_service._check(
            [
                "line 1",
                "line 2",
                "line 3",
            ]
        )

    def test_check_haiku_length_dont_validate_length_2(
        self, haiku_service: HaikuService
    ):
        assert not haiku_service._check(
            [
                "line 1",
                "line 2",
            ]
        )

    def test_check_haiku_length_dont_validate_length_5(
        self, haiku_service: HaikuService
    ):
        assert not haiku_service._check(
            [
                "line 1",
                "line 2",
                "line 3",
                "line 4",
                "line 5",
            ]
        )

    def test_parse_haiku_response(self, haiku_service: HaikuService):
        text = """
            start text
            lorem ipsum
            #####
            line 1
            line 2
            line 3
            #####
            lorem ipsum
            end text
        """
        parsed = haiku_service._parse(text, "#####")
        assert len(parsed) == 3
        assert parsed[0] == "line 1"
        assert parsed[1] == "line 2"
        assert parsed[2] == "line 3"

    def test_parse_haiku_response_without_all_newlines(
        self, haiku_service: HaikuService
    ):
        text = """
            start text
            lorem ipsum
            ##### line 1
            line 2
            line 3 #####
            lorem ipsum
            end text
        """
        parsed = haiku_service._parse(text, "#####")
        assert len(parsed) == 3
        assert parsed[0] == "line 1"
        assert parsed[1] == "line 2"
        assert parsed[2] == "line 3"
