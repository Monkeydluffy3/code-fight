from sphere_engine import CompilersClientV3
from sphere_engine.exceptions import SphereEngineException


T = True
F = False
# define access parameters
accessToken = 'd5549293157f874363dd97c218f73272'
endpoint = '59e166d8.compilers.sphere-engine.com'

# initialization
client = CompilersClientV3(accessToken, endpoint)

# API usage
source = open('file.c','r')
code = source.read();
compiler = 44 # C++14 language
input_val = '5'



try:
    #response = client.submissions.create(code, compiler, input_val)
    #z = response['id']
    #z = int(z)
    z = 66163914
    print(z)
    out = client.submissions.get(z,F,T,T,F,F)
    #print(out)
    str_out = client.submissions.getStream(z, 'output')
    print(str_out)
    
except SphereEngineException as e:
    if e.code == 401:
        print('Invalid access token')