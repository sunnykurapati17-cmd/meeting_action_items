import re,sys,json
P=r'(?i)\b(?:action|todo|to do|will|need to|please)\b[^.\n]*'
def run(t): return [x.strip() for x in re.findall(P,t)]
if __name__=='__main__': print(json.dumps({'action_items':run(open(sys.argv[1]).read() if len(sys.argv)>1 else input('Transcript: '))},indent=2))