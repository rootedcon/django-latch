from latch import Latch
import sys, os

app_id = 'gkWjMpC4ggOKwO5yCijK'
secret = 'o3vdyOzTl9Ny3Rilz3VJiy9mKN9OkMhSDH1Bai1t'
accountId= 'a4ea43f43d1f8a3f1129dfbba4692734e9956e3d7899cc7bd9a742a40284861c'
l = Latch(app_id, secret)

#data = l.pair(sys.argv[1])

data = l.status(accountId)
print "error: %s"% data.get_error()
print "data: %s"% data.get_data()

d = data.get_data()
print d['operations']['gkWjMpC4ggOKwO5yCijK']['status']
