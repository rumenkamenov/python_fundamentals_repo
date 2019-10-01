class Website:
    def __init__(self, host, domain, queries =None):
        self.host = host
        self.domain = domain
        self.queries = self.set_queries(queries)

    def set_queries(self, queries):
        if queries is not None:
            return queries.split(',')
        return None

list_website = []

data = input()

while data != 'end':

    if len(data.split(' | ')) >= 3:
        host, domain, queries = data.split(' | ')
        website = Website(host, domain, queries)
        list_website.append(website)
    else:
        host, domain = data.split(' | ')
        website = Website(host, domain)
        list_website.append(website)

    data = input()


for website in list_website:
        if website.queries is not None:
            print(f'https://www.{website.host}.{website.domain}/query?=[{"]&[".join(website.queries)}]')
        else:
            print(f'https://www.{website.host}.{website.domain}')