from swagger_server.models import InlineResponse2003, StatementsSubject, StatementsObject, StatementsPredicate

def getStatementResponse(c):
    s = StatementsObject('123', 'Lance')
    p = StatementsPredicate('456', 'is cooler than')
    o = StatementsObject('789', 'nearly everyone else')

    responses = [InlineResponse2003(curie, s, p, o) for curie in c]

    print(c)

    return c
