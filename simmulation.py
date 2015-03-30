from __future__ import division
import json
import random
import time
# import numpy
# import redis
import pika
import httplib
import urllib2

headers = {"Content-type": "raw","Accept": "text/plain"}
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs',type='direct')

# def elasticpub(m,t):
# 	conn = httplib.HTTPConnection("localhost:9200")
# 	print m,t
# 	conn.request("POST", "/tracks/cab/"+repr(t),m, headers)
# 	conn.close()

def rabbitpb(m):
	channel.basic_publish(exchange='realtime',routing_key='key',body=m)

# def redispub(m):
# 	r=redis.Redis("192.168.0.49")
# 	r.publish("ch",m)

stops=[[76.8775,8.58548],#"EY Kinfra"
[76.87805,8.5879],#"Vetturoad Junction"
[76.8811,8.58965],#"Kazhakootam Bus Stop"
[76.8834, 8.59172],#"Karyavttom Bus Stop"
[76.888,8.59435],#"Mankuzhi Bus Stop"
[76.8932,8.59702],
[76.8977,8.60335],
[76.8974,8.61786]]
stn=["EY_01",
"EY_GATE_01",
"KUR_01",
"CHA_01",
"KAL_01",
"NAR_01",
"KAT_01",
"POT_01"]
edges={
	"1":[[76.87748,8.58547],[76.87716,8.58647],[76.87707,8.58671],[76.87701,8.58687],[76.87692,8.58703],[76.8769,8.587001],[76.87681,8.58723],[76.87699,8.5872],[76.8772,8.58719],[76.8773,8.5872],[76.87735,8.58722],[76.8774,8.58723],[76.87746,8.58727],[76.87755,8.58734],[76.87797,8.5878],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879],[76.87805,8.5879]],
	"2":[[76.87805,8.5879],[ 76.87823,8.5881],[ 76.87868,8.5886],[ 76.87882,8.58874],[ 76.87898,8.58889],[ 76.87915,8.589020000000001],[ 76.87931,8.58914],[ 76.87949,8.58925],[ 76.8797,8.58938],[ 76.87981000000002,8.58943],[ 76.87993,8.58947],[ 76.88003,8.58951],[ 76.88016000000002,8.58953],[ 76.88028,8.58955],[ 76.88041,8.58956],[ 76.88076,8.58958],[ 76.88087,8.58959],[ 76.88096,8.58961],[ 76.88104,8.58963],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965],[ 76.8811,8.58965]],
	"3":[[76.8811,8.58965],[ 76.88111000000002,8.58965],[ 76.88123,8.5897],[ 76.88136,8.58976],[ 76.8815,8.58984],[ 76.88171,8.59],[ 76.88187,8.59014],[ 76.88204,8.59029],[ 76.8822,8.59045],[ 76.88235,8.59061],[ 76.8825,8.59079],[ 76.88264,8.59094],[ 76.8828,8.59112],[ 76.88284,8.59117],[ 76.88298,8.59132],[ 76.88314,8.59146],[ 76.88337,8.59167],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171],[ 76.88341,8.59171]],
	"4":[[76.88341,8.59171],[ 76.88361,8.59188],[ 76.88384,8.59206],[ 76.88413,8.59226],[ 76.88441,8.59243],[ 76.88464,8.59256],[ 76.8848,8.59265],[ 76.88499,8.59274],[ 76.88528,8.59288],[ 76.88573,8.59309],[ 76.88614000000001,8.59329],[ 76.88644,8.59343],[ 76.88667,8.59354],[ 76.88688,8.59365],[ 76.88712,8.59376],[ 76.88719,8.5938],[ 76.88734,8.59386],[ 76.88755,8.59397],[ 76.88774,8.59406],[ 76.88782,8.59412],[ 76.88788,8.59417],[ 76.88794,8.59422],[ 76.88797,8.59426],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434],[ 76.88802,8.59434]],
	"5":[[76.88802,8.59434],[ 76.88803,8.59436],[ 76.88807,8.59446],[ 76.88813000000002,8.59473],[ 76.88817,8.59492],[ 76.8882,8.59503],[ 76.88823,8.59512],[ 76.88829,8.59526],[ 76.88837,8.59537],[ 76.88846,8.59548],[ 76.88853,8.59555],[ 76.88859,8.59559],[ 76.88864,8.59563],[ 76.8887,8.59566],[ 76.88877,8.59569],[ 76.88892,8.59576],[ 76.88925,8.59585],[ 76.88982,8.59602],[ 76.89036,8.59618],[ 76.89125000000001,8.59645],[ 76.8918,8.59662],[ 76.89217,8.59673],[ 76.89234,8.59678],[ 76.89261,8.59685],[ 76.89288,8.59692],[ 76.89302,8.59697],[ 76.89317,8.59703],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704],[ 76.89319,8.59704]],
	"6":[[76.89319,8.59704],[ 76.89326,8.59707],[ 76.89338,8.59714],[ 76.89347,8.59719],[ 76.89361,8.59728],[ 76.89375,8.59736],[ 76.89387,8.59743],[ 76.89397,8.59747],[ 76.89408,8.59752],[ 76.89417,8.59755],[ 76.89438,8.59762],[ 76.89459,8.5977],[ 76.89491,8.59782],[ 76.89515000000002,8.59792],[ 76.89541000000001,8.59803],[ 76.89562,8.59811],[ 76.89586,8.59822],[ 76.89616,8.59837],[ 76.89658,8.59858],[ 76.89665,8.59864],[ 76.8967,8.59867],[ 76.89675,8.59872],[ 76.89678,8.59875],[ 76.8968,8.59877],[ 76.89681,8.59878],[ 76.89685,8.59883],[ 76.89688,8.59888],[ 76.8969,8.59895],[ 76.89692,8.59901],[ 76.89694,8.59909],[ 76.89695,8.59919],[ 76.89696,8.59936],[ 76.89698,8.59966],[ 76.897,8.5998],[ 76.89701,8.59992],[ 76.89703,8.60002],[ 76.89705,8.60012],[ 76.89708,8.60025],[ 76.89713,8.60038],[ 76.89716,8.60048],[ 76.8972,8.6006],[ 76.89724,8.60073],[ 76.89731,8.60087],[ 76.89737,8.60104],[ 76.89741000000001,8.60118],[ 76.89744,8.60131],[ 76.89746,8.60145],[ 76.8975,8.60164],[ 76.89752,8.60179],[ 76.89754,8.60201],[ 76.89758,8.60229],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.89762,8.60257],[ 76.8977,8.60315],[ 76.89773,8.60335]],
	"7":[[76.89773,8.60335],[ 76.89774,8.60344],[ 76.89775000000002,8.60349],[ 76.89775000000002,8.60355],[ 76.89775000000002,8.6036],[ 76.89775000000002,8.60365],[ 76.89775000000002,8.60375],[ 76.89774,8.60381],[ 76.8977,8.60414],[ 76.89767,8.6045],[ 76.89766,8.60461],[ 76.89764,8.60474],[ 76.89763,8.6048],[ 76.89762,8.60485],[ 76.8976,8.60491],[ 76.89757,8.60498],[ 76.89754,8.60506],[ 76.89751,8.60513],[ 76.89744,8.60527],[ 76.89732000000001,8.60551],[ 76.89722,8.60572],[ 76.89716,8.60583],[ 76.89711,8.60594],[ 76.89707,8.60603],[ 76.89704,8.60612],[ 76.89701,8.6062],[ 76.89696,8.6063],[ 76.89693,8.60641],[ 76.89689,8.606490000000003],[ 76.89685,8.60661],[ 76.89683,8.60667],[ 76.8968,8.60677],[ 76.89677,8.606880000000002],[ 76.89674,8.60698],[ 76.89671000000001,8.60708],[ 76.89667,8.60722],[ 76.89664,8.60733],[ 76.89663,8.60741],[ 76.89661,8.60747],[ 76.89659,8.60756],[ 76.89658,8.60764],[ 76.89657,8.6077],[ 76.89655,8.60776],[ 76.89654,8.60782],[ 76.89654,8.60788],[ 76.89653,8.60796],[ 76.89652,8.60802],[ 76.89652,8.60812],[ 76.89651,8.60824],[ 76.8965,8.60834],[ 76.8965,8.60843],[ 76.89649,8.60852],[ 76.89648,8.6086],[ 76.89646,8.6087],[ 76.89643,8.60885],[ 76.89641,8.60897],[ 76.89639,8.609090000000002],[ 76.89637,8.60921],[ 76.89636,8.60932],[ 76.89635,8.60939],[ 76.89633,8.60954],[ 76.89632,8.60966],[ 76.89628,8.61007],[ 76.89627,8.61028],[ 76.8962,8.61064],[ 76.89617,8.61079],[ 76.89614,8.61094],[ 76.89613,8.61103],[ 76.89612,8.61111],[ 76.89612,8.61113],[ 76.89612,8.61117],[ 76.89612,8.61122],[ 76.89612,8.61126],[ 76.89613,8.61133],[ 76.89614,8.61143],[ 76.89616,8.61154],[ 76.89618,8.61162],[ 76.89623,8.61183],[ 76.89641,8.61254],[ 76.89667,8.613650000000002],[ 76.89679,8.61414],[ 76.89681,8.61419],[ 76.89698,8.61486],[ 76.89715,8.61558],[ 76.89723,8.61592],[ 76.8973,8.61627],[ 76.89733,8.61642],[ 76.89734,8.61655],[ 76.89736,8.61676],[ 76.89736,8.61686],[ 76.89736,8.617],[ 76.89736,8.6171],[ 76.89735,8.61719],[ 76.89729,8.61762],[ 76.89729,8.61768],[ 76.89729,8.61772],[ 76.89728,8.61782],[ 76.89727,8.61789],[ 76.89725,8.61795],[ 76.89724,8.61802],[ 76.89721,8.6181],[ 76.8973,8.61803],[ 76.89733,8.618],[ 76.89736,8.61798],[ 76.89739,8.61796],[ 76.89745,8.61795],[ 76.89738,8.61792],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791],[ 76.89737,8.61791]]
}
path=["1","2","3","4","5","6","7"]

deptimes=[60,200,440,620,860,980,1280,1480]
arrtimes=[180,420,600,840,960,1260,1460,1700]

delta=0.1
def random_mac():
	return "".join([random.choice([repr(i) for i in range(0,10)]+["%c"%(65+i) for i in range(6)]) for _ in range(12)])

def stretch(arr,amt):
	return arr
	polyx=numpy.polyfit(numpy.array(range(len(arr))),numpy.array([arr[i][0] for i in range(len(arr))]),5)
	polyy=numpy.polyfit(numpy.array(range(len(arr))),numpy.array([arr[i][1] for i in range(len(arr))]),5)
	return [[numpy.polyval(polyx,i*len(arr)/amt),numpy.polyval(polyy,i*len(arr)/amt)] for i in range(amt)]

def main():
	t=0
	j=0
	response = urllib2.urlopen('http://localhost:1337/employee/')
	data = json.load(response)
	employees= [data[i][u'name'] for i in range(len(data))]
	for p in range(len(path)):
		brk=json.dumps({"format":"break"})+"\r\n"
		brk+=json.dumps({"broken":{"stop_id":j,"stop_name":stn[j],"timestamp":t,"trip_id":"Kinfra_Pothen_200"}})
		brk+="\r\n"
		print brk
		rabbitpb(brk)
		while t<deptimes[0]:
			time.sleep(delta)
			t+=1
			jsond=json.dumps({"format":"point"})+"\r\n"
			jsond+=(json.dumps({"create":{"_index":"rabbit4","_type":"pin","_id":t}})+"\r\n"+json.dumps({"trip_id":"Kinfra_Pothen_200","timestamp":t,"employees":employees,"location":{"lat":stops[j][1],"lon":stops[j][0]}})+"\r\n")
			print jsond
			#print [stops[j][0],stops[j][1]],","
			rabbitpb(jsond)
			#rabbitpb(json.dumps({"logentry":{"field1":repr(stops[j][0])}}),t)
			#elasticpub(json.dumps({ "pin" : {"location" : { "lat" : stops[j][1], "lon" : stops[j][0] }    } }),t)	
		k=0
		j+=1

		stretched_edge=stretch(edges[path[p]],arrtimes[0]-deptimes[0])
		while t<arrtimes[0]:
			time.sleep(delta)
			t+=1
			jsond=json.dumps({"format":"point"})+"\r\n"
			jsond+=(json.dumps({"create":{"_index":"rabbit4","_type":"pin","_id":t}})+"\r\n"+json.dumps({"trip_id":"Kinfra_Pothen_200","timestamp":t,"employees":employees,"location":{"lat":stretched_edge[k][1],"lon":stretched_edge[k][0]}})+"\r\n")
			print jsond
			#rabbitpb(json.dumps({"vid":1,"Lon":stretched_edge[k][0],"Lat":stretched_edge[k][1],"t":t}))
			rabbitpb(jsond)#1,"Lon":stretched_edge[k][0],"Lat":stretched_edge[k][1],"t":t}))
			#elasticpub(json.dumps({"vid":1,"Lon":stretched_edge[k][0],"Lat":stretched_edge[k][1],"t":t}),t)
			#elasticpub(json.dumps({ "pin" : {"location" : { "lat" : stretched_edge[k][1], "lon" :stretched_edge[k][0]}    } }),t)
			k+=1
		deptimes.pop(0)
		arrtimes.pop(0)
		if random.choice([1,2,3,4,5])==4:
			if len(employees)!=0:
				employees.pop(0)
	brk=json.dumps({"format":"break"})+"\r\n"
	brk+=json.dumps({"broken":{"stop_id":j,"stop_name":stn[j],"timestamp":t}})
	brk+="\r\n"
	print brk
	rabbitpb(brk)
	connection.close()


if __name__=="__main__":
	main()
