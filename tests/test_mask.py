from validkit.mask import mask_secret


def test_mask_secret_keeps_last_four_chars():
    assert mask_secret("geheimnis", keep=4) == "*****mnis"


def test_mask_secret_respects_other_keep_values():
    assert mask_secret("geheimnis", keep=2) == "*******is"
    assert mask_secret("geheimnis", keep=7) == "**heimnis"


def test_mask_secret_keep_zero_masks_everything():
    assert mask_secret("geheimnis", keep=0) == "*********"


def test_mask_secret_keep_too_large_raises_value_error():
    try:
        mask_secret("geheimnis", keep=9)
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for keep >= len(text)")


def test_mask_secret_keep_negative_raises_value_error():
    try:
        mask_secret("geheimnis", keep=-1)
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for negative keep")


def test_mask_secret_empty_text_raises_value_error():
    try:
        mask_secret("", keep=0)
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for empty text")


def test_mask_secret_wrong_type_raises_type_error():
    try:
        mask_secret(12345, keep=4)
    except TypeError:
        pass
    else:
        raise AssertionError("expected TypeError for non-str text")
    try:
        mask_secret("geheimnis", keep="4")
    except TypeError:
        pass
    else:
        raise AssertionError("expected TypeError for non-int keep")


def test_mask_secret_writes_nothing_to_stdout_or_stderr(capsys):
    mask_secret("geheimnis", keep=4)
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
