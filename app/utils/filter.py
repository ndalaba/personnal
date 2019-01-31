def datetimeformat(value, format='%d/%m/%Y %H:%M'):
    if value is None:
        return ''
    return value.strftime(format)
