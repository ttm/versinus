#-*- coding: utf8 -*-
from __future__ import division
import numpy as n, pylab as p, networkx as x, random as r, collections as c, string

__doc__="""Este arquivo possui a classe Sistem, base para todas as animações

G=x.read_gml("1-400cpp.gml") # digrafo com peso
S=Sistem(G)
S.draw("grafo1.png")
S.add_msgs([msg1,msg2...])
S.rm_msgs([msg1,msg2...])
S.order()
S.draw("grafo1.png")

# nadds[i] tem as msgs adicionadas para o frame i+1.
nadds=[[msgs..,..,],[msgs..],[]]
# nrms[i] tem as msgs removidas para o frame i+1.
nrms=[[msgs..,..,],[msgs..],[]]
i=0
for a,r in zip(nadds,nrms):
    S.add_msgs(a)
    S.rm_msgs(b)
    S.order()
    S.draw("grafo%i.png"%(i,))
    i+=1

0) fazer classe com parametros minimos. Fazer com que plote pelo pygraphviz sem layout.
1) fazer classe com parametros minimos. Fazer com que plote pelo pygraphviz com layout pre-determinado.
"""

class Sistem:
    def __init__(self,G="lau300_500.gml",positionMethod="sinusoid",rankCriteria="degree",fixedSize=40):
        """G Digrafo do networkx ou gml para
        
        positionMethod: "random" ou "sinusoid"
        rankCriteria: "alphabetic" ou "degree" """
        self.rank=None
        self.positions=None
        self.ecolors=[]
        if type(G) == type("string"):
            G=x.read_gml(G) # DiGraph
        self.g=G
        self.positionMethod=positionMethod
        self.rankCriteria=rankCriteria
        self.fixedSize=fixedSize
        N=1. # aresta do quadrado considerado
        # ranks nodes in an exact order
        rank=self.rankNodes() # implement
        # gets (x,y) pairs for each ranked node:
        positions=self.positionRanks() 
        ruido=self.computeNoise()

    def update(self):
        self.rankNodes()
        self.positionRanks()

    def addNode(self,nodeName):
        self.g.add_node(nodeName,weight=1.0)
        self.update()
    def addEdge(self,pre,pos):
        self.g.add_edge(pre,pos,weight=1.0)
        self.update()

    def rankNodes(self,force=False):
        """Order nodes in convenient ways to visualisation"""
# order by degree, than by force, than by clustering coefficient, than alphabetically
        if self.rank==None or force:
            print("realizando ordenacao por %s" % (self.rankCriteria,))
            if self.rankCriteria=="alphabetic":
                self.rank=self.g.nodes()
                self.rank.sort()
            elif self.rankCriteria=="degree":
                ordenacao= c.OrderedDict(sorted(dict(self.g.degree()).items(), key=lambda x: -x[1]))
                self.ordenacao=ordenacao
                self.rank=list(ordenacao.keys())
                self.siglas=["G%i"%(i,) for i in ordenacao.values()]
        else:
            print(u"ordenação encontrada. Consulte Sistem.rank.")
        return self.rank

    def positionRanks(self,force=False):
        """Get a position for each of the self.order[i] node
        
        Default is random.
        
        set self.positionMethod to:
            "random",
            "sinusoid" """
        if n.any(self.positions) and not force:
            print("posicoes encontradas, não atualizando posições")
        else:
            print("posicoes nao encontradas, realizando posicionamento para o grafo considerado")
            if self.positionMethod=="random":
                nn=self.g.number_of_nodes()
                loc=n.random.random(nn*2)
                locxy=n.reshape(loc,(nn,2))
            elif self.positionMethod=="sinusoid":
                if self.fixedSize:
                    nn=self.fixedSize
                else:
                    nn=self.g.number_of_nodes()
                xx=n.linspace(0.0,1,nn) # aumentar intervalos primeiros
                parte1=nn/4
                parte2=nn-parte1
                xx=n.hstack( (n.linspace(0.0,0.5,parte1,endpoint=False),n.linspace(0.5,1,parte2)) ) # aumentar intervalos primeiros
                yy=n.sin(xx*2*n.pi) # mudar o numero de voltas
                locxy=n.vstack((xx*4,yy)).T
                sobra = len(self.rank)-locxy.shape[1]
                if sobra < 0:
                    pass
                    #locxy=locxy[:sobra]
                else:
                    poss=n.zeros((2,sobra))
                    #poss[0]+=3.5-n.linspace(0,2,sobra)
                    #poss[1]+=.2+n.linspace(0,2,sobra)
                    parte1=int(sobra/4)
                    parte2=sobra-parte1
                    poss[0]+=n.hstack( (3.5-n.linspace(0,1,parte1), 3.5-n.linspace(1,2,parte2)) )
                    poss[1]+=n.hstack( (.2+n.linspace(0,1,parte1),.2+n.linspace(1,2,parte2)) )
                    locxy=n.hstack( (  locxy.T, poss  )  ).T
            self.positions=locxy
            #positions={}
            #i=0
            #for rank in self.rank:
            #    if i > self.g.number_of_nodes()-self.fixedSize:
            #        positions[rank]=locxy[i -self.g.number_of_nodes()+self.fixedSize ]
            #    else:
            #        positions[rank]=n.array((100,100))
            #    i+=1
            #self.positions=positions
        return self.positions

    def util(self,which="plotpos"):
        if which is "plotpos":
            p.plot(SSi.positions[:,0],SSi.positions[:,1],"bo")
            p.show()

    def draw(self,nome="sistema.png",numero_serie=0):
        p.clf()
        A=x.drawing.nx_agraph.to_agraph(self.g)
        A.node_attr['style']='filled'
        #A.node_attr['fillcolor']='red'
        #A.graph_attr["bgcolor"]="forestgreen"
        A.graph_attr["bgcolor"]="black"
        #A.graph_attr["page"]="31.5,17"
        #A.graph_attr["margin"]="1.7"
        A.graph_attr["pad"]=.1
        A.graph_attr["size"]="9.5,12"
        #A.edge_attr["style"]="solid"
        #A.graph_attr["size"]="55.0,55000.0"
        #A.graph_attr['arrowhead']="diamond"
        #A.graph_attr['dir']="both"
        #A.graph_attr['rankdir']="LR"
        #A.graph_attr['splines']="filled"
        #A.edge_attr.update(arrowType="vec")
        #A.graph_attr['splines']="compound"
        #A.graph_attr['overlap']="true"
        #A.graph_attr['forcelabels']=True
        #A.graph_attr["center"]=1
        #A.layout()
        TTABELACORES=2**10 # tamanho da tabela de cores
        cm=p.cm.Reds(range(TTABELACORES)) # tabela de cores
        #cm=p.cm.hot(range(TTABELACORES)) # tabela de cores
        self.cm=cm
        nodes=A.nodes()
        colors=[]
        loopWeights=[]
        loopnodes=[i[0] for i in self.g.selfloop_edges()]
        self.loopnodes=loopnodes
        # medidas para usar na visualização de cada vértice
        # para largura e altura
        ind=dict(self.g.in_degree(weight='weight')); mind=max(ind.values())/3+0.1
        oud=dict(self.g.out_degree(weight='weight')); moud=max(oud.values())/3+.1
        miod=max(mind,moud)
        #miod=self.g.number_of_edges()+1.
        s=self.g.degree()
        # para colorir
        cc=x.clustering(self.g.to_undirected()) # para colorir
        self.cc=cc
        ii=0
        for node in nodes:
            n_=A.get_node(node)
            if node.isdigit():
                foo=int(node)
            else:
                foo=node
            ifoo=self.rank.index(foo)
            #print ifoo, self.siglas[ifoo]
            n_.attr['fillcolor']= '#%02x%02x%02x' % tuple([int(255*i) for i in cm[int(cc[foo]*255)][:-1]])
            if node in loopnodes:
                loopW=self.g[node][node]["weight"]
                loopWeights.append(loopW)
            else:
                loopW=0
            n_.attr['fixedsize']=True
            #n_.attr['width']=  abs(20*((ind[foo]-loopW)/mind+0.5))
            #n_.attr['height']= abs(20*((oud[foo]-loopW)/moud+0.5))
            n_.attr['width']=  abs(.07*((ind[foo]-loopW)/miod+0.5))
            n_.attr['height']= abs(.07*((oud[foo]-loopW)/miod+0.5))
            #n_.attr['width']=  10*max((ind[int(node)]-loopW)/mind,0.5)
            #n_.attr['height']= 10*max((oud[int(node)]-loopW)/moud,0.5)
            #print("largura, altura: ", n_.attr['width'],n_.attr['height'])
            I=self.rank.index(foo)
            #pos="%f,%f"%tuple(self.positions[ifoo]*300+100); ii+=1
            pos="%f,%f"%tuple(self.positions[ifoo]); ii+=1
            #n_.attr['label']="Q%i"%(ii+1,)
            n_.attr["pos"]=pos
            n_.attr["pin"]=True
            #n_.attr["fontsize"]=1700
            n_.attr["fontsize"]=15
            n_.attr["fontcolor"]="white"

            #n_.attr['label']="%s"%(self.siglas[ifoo],)
            if numero_serie%100<20: # 2 slides a cada 10 slides
                n_.attr['label']="%s"%(self.siglas[ifoo],)
            else:
                n_.attr['label']=""
            #print(pos)
            colors.append('#%02x%02x%02x' % tuple([int(255*i) for i in cm[int(cc[foo]*255)][:-1]]))
        """
        """
        edges=A.edges()
        pesos=[s[2]["weight"] for s in S.g.edges(data=True)]
        self.pesos=pesos
        self.pesos_=[]
        pesosMax=max(pesos)
        self.pesosMax=pesosMax
        for e in edges:
            factor=float(e.attr['weight'])
            self.pesos_.append(factor)
            #e.attr['penwidth']=195*factor
            e.attr['penwidth']=.2*factor
            #e.attr['arrowhead']="diamond"
            #e.attr["arrowsize"]=20
            e.attr["arrowsize"]=.5
            #e.attr['dir']="both"
            #e.attr['dir']="forward"
            #e.attr['rankdir']="LR"
            #e.attr['splines']="curved"
            #e.attr['splines']="compound"
            #e.attr["fontsize"]=4000
            #e.attr['headlabel']="A"
            #e.attr['headlabel']=r"."
            #e.attr["fontcolor"]="red"
            #e.attr["arrowhead"]="both"
            #e.attr["arrowhead"]="vee"
            #e.attr["arrowhead"]="tee"
            #e.attr["arrowhead"]="curve"
            e.attr["arrowhead"]="lteeoldiamond"
            #e.attr["style"]="solid"
            #e.attr["arrowhead"]="diamond"
            #e.attr["arrowtail"]="dot"
            #e.attr["alpha"]=0.2
            w=factor/pesosMax # factor em [0-1]
            #cor=p.cm.hot(int(w*255))
            cor=p.cm.Reds(int(w*255))
            cor=p.cm.Spectral(int(w*255))
            self.cor=cor
            cor256=255*n.array(cor[:-1])

            r0=int(cor256[0]/16)
            r1=int(cor256[0]-r0*16)
            r=hex(r0)[-1]+hex(r1)[-1]

            g0=int(cor256[1]/16)
            g1=int(cor256[1]-g0*16)
            g=hex(g0)[-1]+hex(g1)[-1]

            b0=int(cor256[2]/16)
            b1=int(cor256[2]-b0*16)
            b=hex(b0)[-1]+hex(b1)[-1]

            #corRGB="#"+r+g+b+":#"+r+g+b
            corRGB="#"+r+g+b

            e.attr["color"]=corRGB
            self.ecolors.append(e.attr["color"])
            #e.attr["color"]="white"
            #e.attr["color"]="#0000ff:#ff0000"
        #A.layout(prog="fdp") # fdp ou neato
        label="imagem: %i, |g|= %i, |e|= %i"%(numero_serie,A.number_of_nodes(),A.number_of_edges())
        A.graph_attr["label"]=label
        #A.graph_attr["fontsize"]="1400"


        #### Adicionar nodes nas posicoes relativas a cada posicao
        rank=1
        for pos in self.positions:
            A.add_node(rank)
            n_=A.get_node(rank)
            n_.attr['fixedsize']=True
            n_.attr['width']=  .05
            n_.attr['height']= .05
            n_.attr["pos"]="%f,%f"%tuple(pos);
            if rank < 41:
                n_.attr["pos"]="%f,%f"%(pos[0], -1.2)
            else:
                n_.attr["pos"]="%f,%f"%(pos[0]+.2, pos[1]+.2)
            n_.attr["pin"]=True

            n_.attr["fontsize"]=8.700
            n_.attr["fontcolor"]="white"
            if rank < 41:
                if rank%5==0:
                    n_.attr['label']=str(rank)
                else:
                    n_.attr['label']=""
            else:
                n_.attr['width']=  .03
                n_.attr['height']= .02
                if rank%20==0:
                    n_.attr['label']=str(rank)
                    n_.attr['fontsize']=8
                else:
                    n_.attr['label']=""
            rank+=1
        # adiciona alargador em x:
        #amin=self.positions[:,0].min()
        #amax=self.positions[:,0].max()
        #ambito=amax-amin

        #A.add_node(1000000)
        #n_=A.get_node(1000000)
        #n_.attr['fixedsize']=True
        #n_.attr['width']=  .03
        #n_.attr['height']= .03
        #n_.attr["pos"]="%f,%f"%(amin-.2,-1.1)
        #print n_.attr["pos"]
        #n_.attr['label']=""


        #A.add_node(1000001)
        #n_=A.get_node(1000001)
        #n_.attr['fixedsize']=True
        #n_.attr['width']=.03
        #n_.attr['height']=.03
        #n_.attr["pos"]="%f,%f"%(amax+ambito*.5,-1.1)
        #n_.attr['label']=""

        #A.layout(prog="neato") # fdp ou neato
        #A.draw('%s' % (nome,), prog="fdp") # twopi ou circo
        #A.graph_attr["size"]="15.0,55.0"
        #A.graph_attr["longLabel"]=True
        #A.graph_attr["color"]="gray90"
        A.graph_attr["fontcolor"]="white"
        #A.draw('%s' % (nome,)) # twopi ou circo
        A.draw('%s' % (nome,), prog="neato") # twopi ou circo
        print('scrita figura: %s' % (nome,)) # printando nome
        ################
        # remoção de todos os vertices auxiliares
        self.A=A

        #A.draw('%s' % (nome,),prog="fdp") # twopi ou circo
 
    def computeNoise(self):
        """Count empty messages, empty addressess, swapped messages in time.."""
        pass
#
S=Sistem()
S.draw()
print("escrita figura teste")

#####################
## Roda no ipython
# : run sistema.py
# : S.draw() # cria figura sistema.png
# : run fazRedeInteracao.py # cria g, mm, aa, ids, etc

# : SS=Sistem(g)
# : SS.draw("sistema2.png") # salva no sistema2.png

# : g_=x.DiGraph()
# : SS_=Sistem(g_)
# : SS_.addMsgs([msg1,msg2...])
# : SS_.draw("sistema_.png") # salva no sistema2.png

# : SS_.addMsgs([msg1,msg2...])
# : SS_.rmMsgs([msg1,msg2...])
# : SS_.draw("sistema_2.png") # salva no sistema2.png

#######################################3
######################################3
from dateutil import parser
import mailbox, pytz
utc=pytz.UTC

figs=1
#figs=False
if figs:
    import pylab as p
#caminho="/home/rfabbri/repos/FIM/python/cppStdLib/"
#caminho="/home/rfabbri/repos/FIM/python/lau/"
caminho="/home/rfabbri/repos/FIM/python/lad/"
caminho="/home/renato/repos/versinus/data/gmaneMessages/mbox/lad/"
#caminho="/home/rfabbri/repos/FIM/python/metarec/"
mm={} # dicionário com infos necessárias das msgs
ids=[] # ordem dos ids que apareceram
vz=[] # msgs vazias, para verificação
aa={} # dicionario com autores como chaves, valores sao msgs
ids_r={} # dicionario com chaves que sao ids das msgs aas quais sao resposta
for i in range(1,5001): # soh 500 msgs
    mbox = mailbox.mbox(caminho+str(i))
    if mbox.keys(): # se msg nao vazia
        m=mbox[0]
        au=m['from']
        au=au.replace('"','')
        au=au.split("<")[-1][:-1]
        if " " in au: 
            au=au.split(" ")[0]
        if au not in aa:
            aa[au]=[]
        date=m['date']
        date=date.replace("METDST","MEST")
        date=date.replace("MET DST","MEST")
        #date=date.replace(" CST"," (CST)")
        date=date.replace("(GMT Standard Time)","")
        date=date.replace(" CDT"," (CDT)")
        date=date.replace(" GMT","")
        date=date.replace("(WET DST)","")
        date=date.replace("-0600 CST","-0600")
        #print date
        if "GMT-" in date:
            index=date[::-1].index("-")
            date=date[:-index-1]+")"
        if 'added' in date: date = date.split(" (")[0]
        if m['references']:
            id_ant=m['references'].split('\t')[-1]
            id_ant=id_ant.split(' ')[-1]
        else:
            id_ant=None
        if id_ant not in ids_r.keys():
            ids_r[id_ant]=[]

        date=parser.parse(date)
        try: # colocando localizador em que não tem, para poder comparar
            date=utc.localize(date)
        except:
            pass

        ids_r[id_ant].append( (au,m["message-id"],date) )
        mm[m["message-id"]]=(au,id_ant,date)
        aa[au].append( (m["message-id"], id_ant, date)  )
        ids.append(m['message-id'])
    else:
        vz.append(i)

print("criados aa, mm, vz, ids")

ends=aa.keys()

g=x.DiGraph()

resposta_perdida=[] # para os ids das msgs cuja resposta está perdida
respondido_antes=[]
imgi=0
for i in ids:
    m=mm[i]
    if m[0] in g.nodes():
        if "weight" in g.node[m[0]].keys():
            g.node[m[0]]["weight"]+=1
        else:
            g.add_node(m[0],weight=1.)
            respondido_antes.append(i)
    else:
        g.add_node(m[0],weight=1.)
    if m[1]:
        if m[1] in mm.keys():
            m0=mm[m[1]]

            if g.has_edge(m0[0],m[0]):
                g[m0[0]][m[0]]["weight"]+=1
            else:
                g.add_edge(m0[0], m[0], weight=1.)
        else:
            resposta_perdida.append(i)

print("criado digrafo: g  com todas as mensagens")


print("obtendo lista de vertices e suas siglas")
d=dict(g.degree())
# Vertices ordenados do maior grau para o menor
sequencia=sorted(d, key=d.get, reverse=True)
siglas=["%s" % (d[s],) for s in sequencia]
Si=Sistem(g)
Si.rank=sequencia
Si.siglas=siglas
Si.positionRanks(True)
#Si.positionRanks()
Si.draw("este.png")

#-- G=x.copy.deepcopy(g)
G=g.fresh_copy()
##############################################
print("iniciando animacao")
gg=x.DiGraph()
SSi=Sistem(gg)
SSi.rank=sequencia # preserva ordem e siglas do geral
SSi.siglas=siglas
SSi.positionRanks(True)
JANELA=100
resposta_perdida=[] # para os ids das msgs cuja resposta está perdida
respondido_antes=[]
imgi=0
j=0
m_passadas=[]
for i in ids:
    m=mm[i] ; m_passadas.append(m)
    if m[0] in gg.nodes():
        if "weight" in gg.node[m[0]].keys():
            gg.node[m[0]]["weight"]+=1
        else:
            gg.add_node(m[0],weight=1.)
            respondido_antes.append(i)
    else:
        gg.add_node(m[0],weight=1.)
    if m[1]:
        if m[1] in mm.keys():
            m0=mm[m[1]]

            if gg.has_edge(m0[0],m[0]):
                gg[m0[0]][m[0]]["weight"]+=1
            else:
                gg.add_edge(m0[0], m[0], weight=1.)
        else:
            resposta_perdida.append(i)
    if j>=JANELA:
        # deleta msgs antigas
        m=m_passadas.pop(0)
        if m[0] in gg.nodes():
            if "weight" in gg.node[m[0]].keys():
                if gg.node[m[0]]["weight"]>1:
                    gg.node[m[0]]["weight"]-=1.
                else:
                    if gg.degree()[m[0]]>0:
                        print("deixando vertice permanecer devido aa aresta")
                        gg.node[m[0]]["weight"]-=1.
                    else:
                        print("removendo vertice")
                        gg.remove_node(m[0])
            else:
                print("vertice sem peso, iniciando com peso 0. Msg removida: %i Vertice reinicializado: %s"%(j-JANELA,m[0]))
                gg.node[m[0]]["weight"]=0.
        else:
            print(u"vértice não existente quando procurado para diminuicao de peso: %s"%(m[0],))
        if m[1]: # se é resposta para alguém
            if m[1] in mm.keys():
                m0=mm[m[1]] # mensagem original

                if gg[m0[0]][m[0]]["weight"]>1:
                    gg[m0[0]][m[0]]["weight"]-=1
                else:
                    gg.remove_edge(m0[0], m[0])
                    if gg.degree(m0[0])==0:
                        gg.remove_node(m0[0])
            else:
                resposta_perdida.append(i)
        print("andando com a janela")
    else:
        print("formando janela")

    j+=1
    SSi.update()
    SSi.draw("./v1lad/%05d.png"%(imgi,),imgi); imgi+=1

print("criado digrafo: gg  mensagens")

