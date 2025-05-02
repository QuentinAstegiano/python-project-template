class ComputeService:
    """Service regrouping all compute operation"""

    def _operation(self, index: int, value: int) -> int:
        """A recursive, mostly useless operation"""
        if index == 0:
            return value
        else:
            return value * self._operation(index - 1, value)

    def _simple_compute(self, input: int) -> int:
        """Do a simple operation on the input"""
        return input * 2

    def _complex_compute(self, input: int) -> int:
        """Do a complex operation on the input"""
        return self._operation(2 * input, input)

    def do_compute(self, input: int) -> int:
        """Compute the result of the business operation, given the input"""
        if input % 2 == 0:
            return self._simple_compute(input)
        else:
            return self._complex_compute(input)
