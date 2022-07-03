#!/usr/bin/env python
from exchangelib import Credentials, Account
from exchangelib import OAuth2Credentials
from my_secrets import *

credentials = OAuth2Credentials(
    client_id='d3590ed6-52b3-4102-aeff-aad2292ab01c',
    client_secret='e43fc14f-aa6c-4e2e-beb9-8b5a11533abd',
    tenant_id=my_tenant_id
)

account = Account(my_email, credentials=credentials, autodiscover=True)

for item in account.inbox.all().order_by('-datetime_received')[:100]:
    print(item.subject, item.sender, item.datetime_received)
