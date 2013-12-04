#!/usr/bin/env python
import sys
sys.path.append(".")

from recon.wall import WallReader

for file in sys.argv[1:]:
    with open(file, "rb") as fp:
        wall = WallReader(fp, verbose=True)
        if len(wall.objects()):
            print "No objects"
        else:
            print "Objects:"
        for obj in wall.objects():
            o = wall.read_object(obj)
            print "  "+str(obj)
            print "    Data: "+str(o.data)
            print "    Metadata: "+str(o.metadata)
        
        if len(wall.tables()):
            print "No tables"
        else:
            print "Tables:"
        for tab in wall.tables():
            t = wall.read_table(tab)
            print "  Table: "+str(t)
            print "    Metadata: "+str(t.metadata)
            print "    Signals:"
            for sig in t.signals():
                print "      "+str(sig)
                data = t.data(sig)
                if len(data)<5:
                    print "        Data: "+str(data)
                else:
                    print "        Data: "+str(data[:2]+" ... "+ data[:-2])
                print "        Metadata: "+str(t.vmetadata(sig))
            print "    Aliases:"
            for als in t.aliases():
                print "      "+str(als)
                print "        Alias of: "+str(t.alias_of(als))
                print "        Transform: "+str(t.alias_transform(als))
                print "        Data: "+str(t.data(als))
                print "        Metadata: "+str(t.vmetadata(als))
            
