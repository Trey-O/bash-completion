import pytest

from conftest import TestUnitBase, assert_bash_exec


@pytest.mark.bashcomp(
    cmd=None,
    ignore_env=r"^[+-](COMP(_(WORDS|CWORD|LINE|POINT)|REPLY)|"
    r"cur|cword|words)=",
)
class TestUnitInitCompletion(TestUnitBase):
    def test_1(self, bash):
        """Test environment non-pollution, detected at teardown."""
        assert_bash_exec(
            bash,
            "foo() { "
            "local cur prev words cword "
            "COMP_WORDS=() COMP_CWORD=0 COMP_LINE= COMP_POINT=0; "
            "_init_completion; }; "
            "foo; unset foo",
        )

    def test_2(self, bash):
        output = self._test_unit(
            "_init_completion %s; echo $cur,${prev-}", bash, "(a)", 0, "a", 0
        )
        assert output == ","
