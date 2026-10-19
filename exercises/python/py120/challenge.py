AUDIT_TOTAL = 0

def sum_request(values):
    global AUDIT_TOTAL
    for value in values:
        AUDIT_TOTAL += value
    return AUDIT_TOTAL
