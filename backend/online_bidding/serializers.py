from django.http import HttpResponse
import json
#serializers
def user_profile_serializer(item):
    r = {}
    for i in ['balance','reserved','name_surname']:
        r[i] = getattr(item,i)
    return r
def item_serializer(item):
    r = {}
    for i in ['id','title','description','item_type']:
        r[i] = getattr(item,i)
    r['owner']=user_profile_serializer(item.owner)
    return r
def sell_serializer(sells):
    r = []
    for sell in sells:
        d={}
        for i in ['id','starting','current_price','state']:
            d[i] = getattr(sell,i)
        d['item'] = item_serializer(sell.item)
        r.append(d)
    return r

# Function: success(obj,name)
# Return a successfull result in JSON httpresponse
def success(obj, name):
	return HttpResponse(json.dumps({'result':'Success',name : obj}),
				'text/json')

# Function: error(reason)
# Return a successfull result in JSON
def error(reason):
	return HttpResponse(json.dumps({'result':'Fail','reason' : reason}),
				'text/json')