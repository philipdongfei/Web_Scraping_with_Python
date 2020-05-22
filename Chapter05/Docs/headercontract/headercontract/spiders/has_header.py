from scrapy.contracts import Contract
from scrapy.exceptions import ContractFail


class HasHeaderContract(Contract):
    """Demo contract which checks the presence of a custom header
        @has_header X-CustomHeader
    """

    name = 'has_header'

    def pre_process(self, response):
        for header in self.args:
            if header not in response.headers:
                raise ContractFail('X-CustomHeader not present')

