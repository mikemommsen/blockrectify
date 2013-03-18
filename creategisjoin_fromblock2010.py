
import sys, os

def makegisjoin(block2010):
    return 'G0' + block2010[:2] + '0' + block2010[2:]

def processfile(infile, outdir):
    f = open(infile)
    g = open(os.path.join(outdir,infile), 'w')
    headers = f.readline().strip()
    g.write(headers + 'BLOCKGISJOIN\n')
    for r in f:
        block2010, gradejoin = r.strip().split()
        blockgisjoin = makegisjoin(block2010)
        g.write('{0},{1},{2}'.format(block2010, gradejoin, blockgisjoin))
    f.close()
    g.close()

def run(indir,outdir):
    os.chdir(indir)
    files = os.listdir('.')
    files = [x for x in files if 'BLOCKTOGRADE' in x]
    print files
    for x in files:
        processfile(folder, outdir)

def main():
    indir = sys.argv[1]
    outdir = sys.argv[2]
    run(indir, outdir)
  
    
    
if __name__ == '__main__':
    main()
