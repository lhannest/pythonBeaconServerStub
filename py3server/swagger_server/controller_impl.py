from swagger_server.models import InlineResponse2003, StatementsSubject, StatementsObject, StatementsPredicate

def getStatementResponse(c):
    s = StatementsObject('123', 'concept A')
    p = StatementsPredicate('456', 'relationship')
    o = StatementsObject('789', 'concept B')

    responses = [InlineResponse2003(curie, s, p, o) for curie in c]

    print(c)

    return c
