import warnings
import pytest

from easyexception.exception import easyexception, EasyError


def test_warning_output(caplog):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        easyexception("file.py", "func()", "Warning", "something")
        assert len(w) == 1
        msg = str(w[0].message)
        assert msg.startswith("---Warning: ")


def test_error_raises():
    with pytest.raises(EasyError) as excinfo:
        easyexception("file.py", "func()", "Error", "oops")
    assert "---Error:" in str(excinfo.value)
