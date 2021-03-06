# sfdb - single file database
# © Jose Christian 2022

from json import loads, dumps
from os import path

# make newdb
def mkdb(dbname: str, filedir: str, overwrite=False) -> None:
    if path.isfile(filedir) and overwrite==False:
        print('  sfdb: db file already exists...')
    else:
        # the metadata
        jdata = {
            '_meta': {
                'type': 'sfdb',
                'name': dbname,
                'info': ''
            },
            '_data': {}
        }
        with open(filedir, 'w') as fw:
            fw.write(dumps(jdata, ensure_ascii=False))
    pass

# # # # # # JSON open and save
def openJson(thepath) -> dict:
    with open(thepath, 'r') as fr:
        jdata = loads(fr.read())
    return jdata

def saveJson(jdata, thepath) -> None:
    with open(thepath, 'w') as fw:
        fw.write(dumps(jdata, ensure_ascii=False))
    pass

# # # # # # THIS IS THE CLASS THAT DOES EVERYTHING # # # # # # # # # # #
# the class for the local db
class loaddb():

    def __init__(self, filepath) -> None:
        self.dbdir = filepath
        self.raw = openJson(filepath)
        self.data = self.raw['_data']
        self.name = self.raw['_meta']['name']
        self.info = self.raw['_meta']['info']
        self.dbids = list(self.raw['_data'].keys())
        pass

    # add entry
    def add(self, entid: str, newent: dict) -> None:
        if entid in self.raw['_data']:
            print('  sfdb ERROR: ID "%s" already exists.' % entid)
        elif entid not in self.raw['_data']:
            newent['_dbid'] = entid
            self.raw['_data'][entid] = newent
        pass

    # edit entry
    def edit(self, entid: str, newent: dict) -> None:
        if entid in self.raw['_data']:
            for ek in newent:
                self.raw['_data'][entid][ek] = newent[ek]
        elif entid not in self.raw['_data']:
            print('  sfdb ERROR: ID "%s" not found' % entid)
        pass


    def find(self, searchdict: dict) -> list:

        # declare list output
        listout = []

        for idk in self.raw['_data']:
            ent = self.raw['_data'][idk]
            skey = list(searchdict.keys())[0]
            sval = searchdict[skey]
            if skey in ent:
                if ent[skey]==sval:
                    listout.append(ent)
        return listout

    # save changes to file
    def commit(self) -> None:
        saveJson(self.raw, self.dbdir)
        pass

    # add info
    def addinfo(self, information: str) -> None:
        self.raw['_meta']['info'] = information
        pass

    def get(self, thedbid) -> dict:
        return self.data[thedbid]