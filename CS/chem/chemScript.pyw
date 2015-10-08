try:
    from Tkinter import *
except:
    from tkinter import *
import sqlite3
class elements():
    atomicName=[]
    atomicSymbol=[]
    atomicNumber=[]
    atomicMass=[]
    density=[]
    group=[]
    electronConfiguration=[]
    pelectronegativity=[]
    melectronegativity=[]
    HFusion=[]
    HVaporization=[]
    firstIonizationEnergy=[]
    normalMeltingPoint=[]
    normalBoilingPoint=[]
    
    classOfMetal=[]
    def __init__(self):
        self.atomicName=self.GetInformation('atomicName')#
        self.atomicSymbol=self.GetInformation('atomicSymbol')#
        self.atomicNumber=self.GetInformation('atomicNumber')#
        self.atomicMass=self.GetInformation('atomicMass')#
        self.density=self.GetInformation('density')#
        self.group=self.GetInformation('group')#
        self.pelectronegativity=self.GetInformation('pelectronegativity')
        self.electronConfiguration=self.GetInformation('electronConfiguration')#
    #    self.GetInformation('HFusion')
  #      self.GetInformation('HVaporization')
        self.firstIonizationEnergy=self.GetInformation('firstIonizationEnergy')#
        self.normalMeltingPoint=self.GetInformation('normalMeltingPoint')#
        self.normalBoilingPoint=self.GetInformation('normalBoilingPoint')#
        self.stability=self.GetInformation('stability')#
        for a in range(len(self.electronConfiguration)):
            self.electronConfiguration[a]=self.electronConfiguration[a].replace('<sup>', '')
            self.electronConfiguration[a]=self.electronConfiguration[a].replace('</sup>', '')
            self.atomicMass[a]=float(self.atomicMass[a])
            if self.density[a]!='':
                self.density[a]=float(self.density[a])
            if self.firstIonizationEnergy[a]!='':
                self.firstIonizationEnergy[a]=float(self.firstIonizationEnergy[a])
            if self.normalMeltingPoint[a]!='':
                self.normalMeltingPoint[a]=float(self.normalMeltingPoint[a])
            if self.normalBoilingPoint[a]!='':
                self.normalBoilingPoint[a]=float(self.normalBoilingPoint[a])
    def writeToDatabase(self):
        thoreau = sqlite3.connect('chemTest.db')
        sql=thoreau.cursor()
        sql.execute('''CREATE TABLE IF NOT EXISTS main.elements (atomicName text, atomicSymbol text, atomicNumber text, atomicMass real, density text, periodicgroup text, electronConfig text, pelectronegativity text, melectronegativity text, HFusion text, HVaporization text, firstIonizationEnergy text, normalMeltingPoint text, normalBoilingPoint text, stability text, _ID INTEGER PRIMARY KEY AUTOINCREMENT)''')
        for a in range(len(self.electronConfiguration)):
            sql.execute('''INSERT INTO main.elements (atomicName,
atomicSymbol,
atomicNumber ,
atomicMass ,
density,
periodicgroup,
pelectronegativity,
electronConfig,
melectronegativity,
HFusion,
HVaporization,
firstIonizationEnergy,
normalMeltingPoint,
normalBoilingPoint,
stability) VALUES (
?,
?,
?,
?,
?,
?,
?,
?,
'',
'',
'',
?,
?,
?,
?)
''', [self.atomicName[a], self.atomicSymbol[a], self.atomicNumber[a], self.atomicMass[a], self.density[a], self.group[a], self.pelectronegativity[a], self.electronConfiguration[a], self.firstIonizationEnergy[a], self.normalMeltingPoint[a], self.normalBoilingPoint[a], self.stability[a]])
        thoreau.commit()
        sql.close()
        thoreau.close()
    def SaveInformation(self, thingToStore, propertiesListByElement):
        toWrite = open(r''+thingToStore + '.ele', 'w')
        outString=''
        for x in propertiesListByElement:
            outString+=x+'\n'
        toWrite.write(outString)
        toWrite.close()
    def GetInformation(self, thingToGet):
        toGet =  open(r'' + thingToGet + '.ele', 'r')
        propertiesListByElement=[]
        while True:
            data = toGet.readline()
            if not data:
                break
            else:
                #print "%s\t@%s@" %(thingToGet, data[:len(data)-1])
                propertiesListByElement.append(data[:len(data)-1])
        return propertiesListByElement

    def OutputTable(self):
        outString=""
        outGrid=[]
        #outString=outString+ string.format("%s%s%s%s%s%s%s%s%s%s%s%s\n" %("Name".rjust(14), "#".rjust(4), "Sym".rjust(4), "Mass".rjust(10), "g/cm^3".rjust(8), "group".rjust(6), "electron Configuration".rjust(23), "1st Ion".rjust(8), "melt".rjust(8), "Boil".rjust(8), "unstable".rjust(8), "enegativity".rjust(13)))
        for i in range(len(self.atomicName)):
        #     outString= outString+string.format("%s%s%s%s%s%s%s%s%s%s%s%s\n" %(self.atomicName[i].rjust(14), self.atomicNumber[i].rjust(4), self.atomicSymbol[i].rjust(4), str(self.atomicMass[i]).rjust(8), str(self.density[i]).rjust(8), self.group[i].rjust(6), str(self.electronConfiguration[i]).rjust(23), str(self.firstIonizationEnergy[i]).rjust(8), str(self.normalMeltingPoint[i]).rjust(8), str(self.normalBoilingPoint[i]).rjust(8), self.stability[i].rjust(8), str(self.penegativity[i]).rjust(13)))
            outRow=[self.atomicName[i], self.atomicNumber[i], self.atomicSymbol[i], self.atomicMass[i], self.density[i], self.group[i], self.electronConfiguration[i], self.firstIonizationEnergy[i], self.normalMeltingPoint[i], self.normalBoilingPoint[i], self.stability[i], self.pelectronegativity[i]]
            outGrid.append(outRow)
        return outGrid
    def GetElementInfo(self, el2):
        theAtomicNumber=-1
        if isinstance(el2, int) or el2.isdigit():
            for k, v in enumerate(self.atomicNumber):
                if v==str(el2):
                    theAtomicNumber=k
        elif len(el2)<3:
            for k, v in enumerate(self.atomicSymbol):
                if v==el2:
                    theAtomicNumber=k
        else:
            for k, v in enumerate(self.atomicName):
                if v.lower()==el2.lower():
                    theAtomicNumber=k
        if theAtomicNumber>=0:
            return self.GetInfo(theAtomicNumber)
        else:
            return ["couldn't find the element\n"]
    def FindByMass(self, mass, accuracy=1):
        theAtomicNumber=[]
        for k, v in enumerate(self.atomicMass):
                if abs(v-mass)<accuracy:
                    theAtomicNumber.append(k)
        if len(theAtomicNumber)>0:
            return self.GetArrayInfo(theAtomicNumber)
        else:
            return "couldn't find the element\n"           
    def FindByDensity(self, density, accuracy=1):
        theAtomicNumber=[]
        if not isinstance(density, float):
            return [["couldn't find the element"]]
        else:
            for k, v in enumerate(self.density):
                if str(v)!='':
                    if abs(v-density)<accuracy and v!=0:
                        theAtomicNumber.append(k)
            if len(theAtomicNumber)>0:
                return self.GetArrayInfo(theAtomicNumber)
            else:
                return ["couldn't find the element\n"]
    def GetArrayInfo(self, array):
        #outputString=format("%s%s%s%s%s%s%s%s%s%s%s%s\n" %("Name".rjust(14), "#".rjust(4), "Sym".rjust(4), "Mass".rjust(8), "g/cm^3".rjust(8), "group".rjust(6), "electron Configuration".rjust(23), "1st Ion".rjust(8), "melt".rjust(8), "Boil".rjust(8), "unstable".rjust(8), "enegativity".rjust(13)))
        outGrid=[]
        for i in array:
            outRow=[self.atomicName[i], self.atomicNumber[i], self.atomicSymbol[i], self.atomicMass[i], self.density[i], self.group[i], self.electronConfiguration[i], self.firstIonizationEnergy[i], self.normalMeltingPoint[i], self.normalBoilingPoint[i], self.stability[i], self.pelectronegativity[i]]
            outGrid.append(outRow)
            #outputString=outputString+format("%s%s%s%s%s%s%s%s%s%s%s%s\n" %(self.atomicName[i].rjust(14), self.atomicNumber[i].rjust(4), self.atomicSymbol[i].rjust(4), str(self.atomicMass[i]).rjust(8), str(self.density[i]).rjust(8), self.group[i].rjust(6), str(self.electronConfiguration[i]).rjust(23), str(self.firstIonizationEnergy[i]).rjust(8), str(self.normalMeltingPoint[i]).rjust(8), str(self.normalBoilingPoint[i]).rjust(8), self.stability[i].rjust(8), str(self.pelectronegativity[i]).rjust(13)))
        return outGrid
    def GetInfo(self, i):
        outGrid=[]
        outRow=[self.atomicName[i], self.atomicNumber[i], self.atomicSymbol[i], self.atomicMass[i], self.density[i], self.group[i], self.electronConfiguration[i], self.firstIonizationEnergy[i], self.normalMeltingPoint[i], self.normalBoilingPoint[i], self.stability[i], self.pelectronegativity[i]]
        outGrid.append(outRow)
        return outGrid
        #return outputString
    def GetElectronegativityDifference(self, el1, el2):
        theAtomicNumber=-1
        if isinstance(el1, int) or el1.isdigit():
            for k, v in enumerate(self.atomicNumber):
                if v==str(el1):
                    theAtomicNumber=k
        elif len(el1)<3:
            for k, v in enumerate(self.atomicSymbol):
                if v==el1:
                    theAtomicNumber=k
        else:
            for k, v in enumerate(self.atomicName):
                if v==el1:
                    theAtomicNumber=k
        if theAtomicNumber>=0:
            el1Eneg=self.pelectronegativity[theAtomicNumber]
        else:
            return "couldn't find the element\n"
            el1Eneg=-1
        theAtomicNumber=-1
        if isinstance(el2, int) or el2.isdigit():
            for k, v in enumerate(self.atomicNumber):
                if v==str(el2):
                    theAtomicNumber=k
        elif len(el2)<3:
            for k, v in enumerate(self.atomicSymbol):
                if v==el2:
                    theAtomicNumber=k
        else:
            for k, v in enumerate(self.atomicName):
                if v==el2:
                    theAtomicNumber=k
        if theAtomicNumber>=0:
            el2Eneg=self.pelectronegativity[theAtomicNumber]
        else:
            return "couldn't find the element\n"
            el2Eneg=-1
        if(float(el1Eneg)>=0 and float(el2Eneg)>=0):
            return ["{: 03.2f}".format(float(el2Eneg)-float(el1Eneg)), "{: 03.2f}".format(float(el2Eneg))]
        else:
            return -1
    def orderByEnegDiff(self, elmntInQuestion, elmntArray):
        outList=[]
        for  i in elmntArray:
            eDiff=self.GetElectronegativityDifference(elmntInQuestion, i)
            if len(outList)==0:
                outList.append([i, eDiff[0], eDiff[1]])
            else:
                boolean = False
                for j in range(len(outList)):
                    if eDiff[0]< outList[j][1] and boolean==False:
                            boolean = True
                            outList.insert(j, [i, eDiff[0], eDiff[1]])
                    else:
                        if(j+1==len(outList)) and boolean==False:
                            outList.append([i, eDiff[0], eDiff[1]])
                            boolean = True
        toCompare = self.GetElectronegativityDifference(elmntInQuestion, elmntInQuestion)
        outList.insert(0, [elmntInQuestion, toCompare[0], toCompare[1]])
        return outList
        #self.printEnegDiff(outList)
    def printEnegDiff(self, outList):
        outstring=''
        for i in range(len(outList)):
            outstring = outstring + format("%s\t%.3f\n" %(outList[i][0], outList[i][1]))
        return outstring

class App:
    def __init__(self):
        self.elChart=elements()
        self.root= Tk()
        self.root.title("Elementary Calculations")
        try:
            self.root.wm_iconbitmap("App-katomic-atom.ico")
        except:
            try:
                self.root.iconbitmap('App-katomic-atom.ico')
            except:
                pass
        self.text = StringVar()
        self.unc = StringVar()
        self.frame = Frame(self.root)
        self.frame.grid()
        self.toSearch=StringVar()
        self.eneg = Button(self.frame, text="ENEG", command=self.enegParse)
        self.eneg.grid(row=2, column=0)
        self.button = Button(self.frame, text="QUIT", fg="red", command=self.quit)
        self.uncertainty = Entry(self.frame, textvariable=self.unc)
        self.uncertainty.grid(row=2, column=2)
        self.uncertaintylabel = Label(self.frame, text="(+/-)")
        self.uncertaintylabel.grid(row=2, column=1)
        self.searchLabel=Label(self.frame, text="Element Info")
        self.searchLabel.grid(row=1, column=1)
        self.searchBar = Entry(self.frame, fg="#000", bg="#0f0", textvariable=self.toSearch)
        self.searchBar.bind("<Return>", self.callHither)
        self.searchBar.grid(row=1, column=2)
        self.button.grid(row=0, column=0)
        self.findByMass=Button(self.frame, text="Mass", command=self.findByMass)
        self.findByMass.grid(row=1, column=0)
        self.findByDensity=Button(self.frame, text="Density", command=self.findByDense)
        self.findByDensity.grid(row=0, column=2, sticky=N+E+W+S)
        self.hi_there=Button(self.frame, text="Name, #, Symbol", command=self.say_hi)
        self.hi_there.grid(row=0, column=1)
#        self.label=Label(self.frame, textvariable=self.text)
#        self.label.grid(row=0, rowspan=3, column=3, sticky=N)
        gerschwin="garganzola"
        self.text.set(gerschwin)
        self.root.mainloop()#This needs to be last
    def callHither(self, args):
        pot=self.toSearch.get()
        if " " in pot:
            self.enegParse()
        else:
            self.say_hi()
    def hitReturn(self):
        True
    def enegUpdateBox(self, x):
        if(hasattr(self, 'innerFrame')):
            self.innerFrame.grid_forget()
            self.innerFrame.destroy()
        self.innerFrame= Frame(self.frame)
        self.innerFrame.grid(row=0, rowspan=3, column=3, sticky=N)
        x.insert(0, ["Name", "Relative Electronegativity", "Absolute Electronegativity"])
        for k, v in enumerate(x):
            for key, value in enumerate(v):
                best=StringVar()
                best.set(value)
                if (k != 0 and float(v[1]) > .3):
                    textBox=Label(self.innerFrame, textvariable= best, fg="red")
                    textBox.grid(row=k, column=key)
                else:
                    if(k != 0 and float(v[1])<-.3):
                        textBox=Label(self.innerFrame, textvariable= best, fg="blue")
                        textBox.grid(row=k, column=key)
                    else:
                        textBox=Label(self.innerFrame, textvariable= best)
                        textBox.grid(row=k, column=key)
        #self.text.set()
    def updateReturnBox(self, x):
        if(hasattr(self, 'innerFrame')):
            self.innerFrame.grid_forget()
            self.innerFrame.destroy()
        self.innerFrame= Frame(self.frame)
        self.innerFrame.grid(row=0, rowspan=3, column=3, sticky=N)
        x.insert(0, ["Name", "#", "Sym", "Mass", "g/cm^3", "group", "electron Configuration", "1st Ion", "Melt", "Boil", "unstable", "electronegativity"])
        for k, v in enumerate(x):
            for key, value in enumerate(v):
                best=StringVar()
                best.set(value)
                textBox=Label(self.innerFrame, textvariable= best)
                textBox.grid(row=k, column=key)
        #self.text.set()
    def findByMass(self):
        accuracy=self.unc.get()
        mass=self.toSearch.get()
        if accuracy=='':
            accuracy = 1
        if mass=='':
            self.text.set("Please enter a density in the green box and try again")
        else:
            mass=self.toSearch.get()
            x= self.elChart.FindByMass(float(mass), float(accuracy))
            self.updateReturnBox(x)
    def enegParse(self):
        elToComp=self.toSearch.get().split(' ')
        self.enegUpdateBox(self.elChart.orderByEnegDiff(elToComp[0], elToComp[1:]))
        
    def findByDense(self):
        accuracy=self.unc.get()
        density=self.toSearch.get()
        if accuracy=='':
            accuracy = 1
        if density=='':
            self.text.set("Please enter a density in the green box and try again")
        else:
            density=self.toSearch.get()
            try:
                density = float(density)
                self.updateReturnBox(self.elChart.FindByDensity(float(density), float(accuracy)))
            except ValueError:
                self.updateReturnBox([["couldn't find the element"]])
    def SearchElements(self):
        toFind = self.searchBar.text
    def quit(self):
        self.root.destroy()
    def say_hi(self):
        pot=self.toSearch.get()
        pot=self.elChart.GetElementInfo(pot)
        self.updateReturnBox(pot)
        #self.label=self.text.get()
app=App()

##Storing info here for now
#    periodicTable="""<tr><td>1</td><td></td><td>1.0079</td><td>Hydrogen</td><td>H</td><td>-259</td><td>-253</td><td>0.09</td><td>0.14</td><td>1776</td><td>1</td><td>1s<sup>1</sup></td><td>13.5984</td></tr><tr class="bkgcyan"><td>2</td><td></td><td>4.0026</td><td>Helium</td><td>He</td><td>-272</td><td>-269</td><td>0.18</td><td></td><td>1895</td><td>18</td><td>1s<sup>2</sup></td><td>24.5874</td></tr><tr><td>3</td><td></td><td>6.941</td><td>Lithium</td><td>Li</td><td>180</td><td>1347</td><td>0.53</td><td></td><td>1817</td><td>1</td><td>[He] 2s<sup>1</sup></td><td>5.3917</td></tr><tr class="bkgcyan"><td>4</td><td></td><td>9.0122</td><td>Beryllium</td><td>Be</td><td>1278</td><td>2970</td><td>1.85</td><td></td><td>1797</td><td>2</td><td>[He] 2s<sup>2</sup></td><td>9.3227</td></tr><tr><td>5</td><td></td><td>10.811</td><td>Boron</td><td>B</td><td>2300</td><td>2550</td><td>2.34</td><td></td><td>1808</td><td>13</td><td>[He] 2s<sup>2</sup> 2p<sup>1</sup></td><td>8.298</td></tr><tr class="bkgcyan"><td>6</td><td></td><td>12.0107</td><td>Carbon</td><td>C</td><td>3500</td><td>4827</td><td>2.26</td><td>0.094</td><td> ancient</td><td>14</td><td>[He] 2s<sup>2</sup> 2p<sup>2</sup></td><td>11.2603</td></tr><tr><td>7</td><td></td><td>14.0067</td><td>Nitrogen</td><td>N</td><td>-210</td><td>-196</td><td>1.25</td><td></td><td>1772</td><td>15</td><td>[He] 2s<sup>2</sup> 2p<sup>3</sup></td><td>14.5341</td></tr><tr class="bkgcyan"><td>8</td><td></td><td>15.9994</td><td>Oxygen</td><td>O</td><td>-218</td><td>-183</td><td>1.43</td><td>46.71</td><td>1774</td><td>16</td><td>[He] 2s<sup>2</sup> 2p<sup>4</sup></td><td>13.6181</td></tr><tr><td>9</td><td></td><td>18.9984</td><td>Fluorine</td><td>F</td><td>-220</td><td>-188</td><td>1.7</td><td>0.029</td><td>1886</td><td>17</td><td>[He] 2s<sup>2</sup> 2p<sup>5</sup></td><td>17.4228</td></tr><tr class="bkgcyan"><td>10</td><td></td><td>20.1797</td><td>Neon</td><td>Ne</td><td>-249</td><td>-246</td><td>0.9</td><td></td><td>1898</td><td>18</td><td>[He] 2s<sup>2</sup> 2p<sup>6</sup></td><td>21.5645</td></tr><tr><td>11</td><td></td><td>22.9897</td><td>Sodium</td><td>Na</td><td>98</td><td>883</td><td>0.97</td><td>2.75</td><td>1807</td><td>1</td><td>[Ne] 3s<sup>1</sup></td><td>5.1391</td></tr><tr class="bkgcyan"><td>12</td><td></td><td>24.305</td><td>Magnesium</td><td>Mg</td><td>639</td><td>1090</td><td>1.74</td><td>2.08</td><td>1755</td><td>2</td><td>[Ne] 3s<sup>2</sup></td><td>7.6462</td></tr><tr><td>13</td><td></td><td>26.9815</td><td>Aluminum</td><td>Al</td><td>660</td><td>2467</td><td>2.7</td><td>8.07</td><td>1825</td><td>13</td><td>[Ne] 3s<sup>2</sup> 3p<sup>1</sup></td><td>5.9858</td></tr><tr class="bkgcyan"><td>14</td><td></td><td>28.0855</td><td>Silicon</td><td>Si</td><td>1410</td><td>2355</td><td>2.33</td><td>27.69</td><td>1824</td><td>14</td><td>[Ne] 3s<sup>2</sup> 3p<sup>2</sup></td><td>8.1517</td></tr><tr><td>15</td><td></td><td>30.9738</td><td>Phosphorus</td><td>P</td><td>44</td><td>280</td><td>1.82</td><td>0.13</td><td>1669</td><td>15</td><td>[Ne] 3s<sup>2</sup> 3p<sup>3</sup></td><td>10.4867</td></tr><tr class="bkgcyan"><td>16</td><td></td><td>32.065</td><td>Sulfur</td><td>S</td><td>113</td><td>445</td><td>2.07</td><td>0.052</td><td> ancient</td><td>16</td><td>[Ne] 3s<sup>2</sup> 3p<sup>4</sup></td><td>10.36</td></tr><tr><td>17</td><td></td><td>35.453</td><td>Chlorine</td><td>Cl</td><td>-101</td><td>-35</td><td>3.21</td><td>0.045</td><td>1774</td><td>17</td><td>[Ne] 3s<sup>2</sup> 3p<sup>5</sup></td><td>12.9676</td></tr><tr class="bkgcyan"><td>18</td><td></td><td>39.948</td><td>Argon</td><td>Ar</td><td>-189</td><td>-186</td><td>1.78</td><td></td><td>1894</td><td>18</td><td>[Ne] 3s<sup>2</sup> 3p<sup>6</sup></td><td>15.7596</td></tr><tr><td>19</td><td></td><td>39.0983</td><td>Potassium</td><td>K</td><td>64</td><td>774</td><td>0.86</td><td>2.58</td><td>1807</td><td>1</td><td>[Ar] 4s<sup>1</sup></td><td>4.3407</td></tr><tr class="bkgcyan"><td>20</td><td></td><td>40.078</td><td>Calcium</td><td>Ca</td><td>839</td><td>1484</td><td>1.55</td><td>3.65</td><td>1808</td><td>2</td><td>[Ar] 4s<sup>2</sup></td><td>6.1132</td></tr><tr><td>21</td><td></td><td>44.9559</td><td>Scandium</td><td>Sc</td><td>1539</td><td>2832</td><td>2.99</td><td></td><td>1879</td><td>3</td><td>[Ar] 3d<sup>1</sup> 4s<sup>2</sup></td><td>6.5615</td></tr><tr class="bkgcyan"><td>22</td><td></td><td>47.867</td><td>Titanium</td><td>Ti</td><td>1660</td><td>3287</td><td>4.54</td><td>0.62</td><td>1791</td><td>4</td><td>[Ar] 3d<sup>2</sup> 4s<sup>2</sup></td><td>6.8281</td></tr><tr><td>23</td><td></td><td>50.9415</td><td>Vanadium</td><td>V</td><td>1890</td><td>3380</td><td>6.11</td><td></td><td>1830</td><td>5</td><td>[Ar] 3d<sup>3</sup> 4s<sup>2</sup></td><td>6.7462</td></tr><tr class="bkgcyan"><td>24</td><td></td><td>51.9961</td><td>Chromium</td><td>Cr</td><td>1857</td><td>2672</td><td>7.19</td><td>0.035</td><td>1797</td><td>6</td><td>[Ar] 3d<sup>5</sup> 4s<sup>1</sup></td><td>6.7665</td></tr><tr><td>25</td><td></td><td>54.938</td><td>Manganese</td><td>Mn</td><td>1245</td><td>1962</td><td>7.43</td><td>0.09</td><td>1774</td><td>7</td><td>[Ar] 3d<sup>5</sup> 4s<sup>2</sup></td><td>7.434</td></tr><tr class="bkgcyan"><td>26</td><td></td><td>55.845</td><td>Iron</td><td>Fe</td><td>1535</td><td>2750</td><td>7.87</td><td>5.05</td><td> ancient</td><td>8</td><td>[Ar] 3d<sup>6</sup> 4s<sup>2</sup></td><td>7.9024</td></tr><tr><td>27</td><td></td><td>58.9332</td><td>Cobalt</td><td>Co</td><td>1495</td><td>2870</td><td>8.9</td><td></td><td>1735</td><td>9</td><td>[Ar] 3d<sup>7</sup> 4s<sup>2</sup></td><td>7.881</td></tr><tr class="bkgcyan"><td>28</td><td></td><td>58.6934</td><td>Nickel</td><td>Ni</td><td>1453</td><td>2732</td><td>8.9</td><td>0.019</td><td>1751</td><td>10</td><td>[Ar] 3d<sup>8</sup> 4s<sup>2</sup></td><td>7.6398</td></tr><tr><td>29</td><td></td><td>63.546</td><td>Copper</td><td>Cu</td><td>1083</td><td>2567</td><td>8.96</td><td></td><td> ancient</td><td>11</td><td>[Ar] 3d<sup>10</sup> 4s<sup>1</sup></td><td>7.7264</td></tr><tr class="bkgcyan"><td>30</td><td></td><td>65.39</td><td>Zinc</td><td>Zn</td><td>420</td><td>907</td><td>7.13</td><td></td><td> ancient</td><td>12</td><td>[Ar] 3d<sup>10</sup> 4s<sup>2</sup></td><td>9.3942</td></tr><tr><td>31</td><td></td><td>69.723</td><td>Gallium</td><td>Ga</td><td>30</td><td>2403</td><td>5.91</td><td></td><td>1875</td><td>13</td><td>[Ar] 3d<sup>10</sup> 4s<sup>2</sup> 4p<sup>1</sup></td><td>5.9993</td></tr><tr class="bkgcyan"><td>32</td><td></td><td>72.64</td><td>Germanium</td><td>Ge</td><td>937</td><td>2830</td><td>5.32</td><td></td><td>1886</td><td>14</td><td>[Ar] 3d<sup>10</sup> 4s<sup>2</sup> 4p<sup>2</sup></td><td>7.8994</td></tr><tr><td>33</td><td></td><td>74.9216</td><td>Arsenic</td><td>As</td><td>81</td><td>613</td><td>5.72</td><td></td><td> ancient</td><td>15</td><td>[Ar] 3d<sup>10</sup> 4s<sup>2</sup> 4p<sup>3</sup></td><td>9.7886</td></tr><tr class="bkgcyan"><td>34</td><td></td><td>78.96</td><td>Selenium</td><td>Se</td><td>217</td><td>685</td><td>4.79</td><td></td><td>1817</td><td>16</td><td>[Ar] 3d<sup>10</sup> 4s<sup>2</sup> 4p<sup>4</sup></td><td>9.7524</td></tr><tr><td>35</td><td></td><td>79.904</td><td>Bromine</td><td>Br</td><td>-7</td><td>59</td><td>3.12</td><td></td><td>1826</td><td>17</td><td>[Ar] 3d<sup>10</sup> 4s<sup>2</sup> 4p<sup>5</sup></td><td>11.8138</td></tr><tr class="bkgcyan"><td>36</td><td></td><td>83.8</td><td>Krypton</td><td>Kr</td><td>-157</td><td>-153</td><td>3.75</td><td></td><td>1898</td><td>18</td><td>[Ar] 3d<sup>10</sup> 4s<sup>2</sup> 4p<sup>6</sup></td><td>13.9996</td></tr><tr><td>37</td><td></td><td>85.4678</td><td>Rubidium</td><td>Rb</td><td>39</td><td>688</td><td>1.63</td><td></td><td>1861</td><td>1</td><td>[Kr] 5s<sup>1</sup></td><td>4.1771</td></tr><tr class="bkgcyan"><td>38</td><td></td><td>87.62</td><td>Strontium</td><td>Sr</td><td>769</td><td>1384</td><td>2.54</td><td></td><td>1790</td><td>2</td><td>[Kr] 5s<sup>2</sup></td><td>5.6949</td></tr><tr><td>39</td><td></td><td>88.9059</td><td>Yttrium</td><td>Y</td><td>1523</td><td>3337</td><td>4.47</td><td></td><td>1794</td><td>3</td><td>[Kr] 4d<sup>1</sup> 5s<sup>2</sup></td><td>6.2173</td></tr><tr class="bkgcyan"><td>40</td><td></td><td>91.224</td><td>Zirconium</td><td>Zr</td><td>1852</td><td>4377</td><td>6.51</td><td>0.025</td><td>1789</td><td>4</td><td>[Kr] 4d<sup>2</sup> 5s<sup>2</sup></td><td>6.6339</td></tr><tr><td>41</td><td></td><td>92.9064</td><td>Niobium</td><td>Nb</td><td>2468</td><td>4927</td><td>8.57</td><td></td><td>1801</td><td>5</td><td>[Kr] 4d<sup>4</sup> 5s<sup>1</sup></td><td>6.7589</td></tr><tr class="bkgcyan"><td>42</td><td></td><td>95.94</td><td>Molybdenum</td><td>Mo</td><td>2617</td><td>4612</td><td>10.22</td><td></td><td>1781</td><td>6</td><td>[Kr] 4d<sup>5</sup> 5s<sup>1</sup></td><td>7.0924</td></tr><tr><td>43</td><td>*</td><td>98</td><td>Technetium</td><td>Tc</td><td>2200</td><td>4877</td><td>11.5</td><td></td><td>1937</td><td>7</td><td>[Kr] 4d<sup>5</sup> 5s<sup>2</sup></td><td>7.28</td></tr><tr class="bkgcyan"><td>44</td><td></td><td>101.07</td><td>Ruthenium</td><td>Ru</td><td>2250</td><td>3900</td><td>12.37</td><td></td><td>1844</td><td>8</td><td>[Kr] 4d<sup>7</sup> 5s<sup>1</sup></td><td>7.3605</td></tr><tr><td>45</td><td></td><td>102.9055</td><td>Rhodium</td><td>Rh</td><td>1966</td><td>3727</td><td>12.41</td><td></td><td>1803</td><td>9</td><td>[Kr] 4d<sup>8</sup> 5s<sup>1</sup></td><td>7.4589</td></tr><tr class="bkgcyan"><td>46</td><td></td><td>106.42</td><td>Palladium</td><td>Pd</td><td>1552</td><td>2927</td><td>12.02</td><td></td><td>1803</td><td>10</td><td>[Kr] 4d<sup>10</sup></td><td>8.3369</td></tr><tr><td>47</td><td></td><td>107.8682</td><td>Silver</td><td>Ag</td><td>962</td><td>2212</td><td>10.5</td><td></td><td> ancient</td><td>11</td><td>[Kr] 4d<sup>10</sup> 5s<sup>1</sup></td><td>7.5762</td></tr><tr class="bkgcyan"><td>48</td><td></td><td>112.411</td><td>Cadmium</td><td>Cd</td><td>321</td><td>765</td><td>8.65</td><td></td><td>1817</td><td>12</td><td>[Kr] 4d<sup>10</sup> 5s<sup>2</sup></td><td>8.9938</td></tr><tr><td>49</td><td></td><td>114.818</td><td>Indium</td><td>In</td><td>157</td><td>2000</td><td>7.31</td><td></td><td>1863</td><td>13</td><td>[Kr] 4d<sup>10</sup> 5s<sup>2</sup> 5p<sup>1</sup></td><td>5.7864</td></tr><tr class="bkgcyan"><td>50</td><td></td><td>118.71</td><td>Tin</td><td>Sn</td><td>232</td><td>2270</td><td>7.31</td><td></td><td> ancient</td><td>14</td><td>[Kr] 4d<sup>10</sup> 5s<sup>2</sup> 5p<sup>2</sup></td><td>7.3439</td></tr><tr><td>51</td><td></td><td>121.76</td><td>Antimony</td><td>Sb</td><td>630</td><td>1750</td><td>6.68</td><td></td><td> ancient</td><td>15</td><td>[Kr] 4d<sup>10</sup> 5s<sup>2</sup> 5p<sup>3</sup></td><td>8.6084</td></tr><tr class="bkgcyan"><td>52</td><td></td><td>127.6</td><td>Tellurium</td><td>Te</td><td>449</td><td>990</td><td>6.24</td><td></td><td>1783</td><td>16</td><td>[Kr] 4d<sup>10</sup> 5s<sup>2</sup> 5p<sup>4</sup></td><td>9.0096</td></tr><tr><td>53</td><td></td><td>126.9045</td><td>Iodine</td><td>I</td><td>114</td><td>184</td><td>4.93</td><td></td><td>1811</td><td>17</td><td>[Kr] 4d<sup>10</sup> 5s<sup>2</sup> 5p<sup>5</sup></td><td>10.4513</td></tr><tr class="bkgcyan"><td>54</td><td></td><td>131.293</td><td>Xenon</td><td>Xe</td><td>-112</td><td>-108</td><td>5.9</td><td></td><td>1898</td><td>18</td><td>[Kr] 4d<sup>10</sup> 5s<sup>2</sup> 5p<sup>6</sup></td><td>12.1298</td></tr><tr><td>55</td><td></td><td>132.9055</td><td>Cesium</td><td>Cs</td><td>29</td><td>678</td><td>1.87</td><td></td><td>1860</td><td>1</td><td>[Xe] 6s<sup>1</sup></td><td>3.8939</td></tr><tr class="bkgcyan"><td>56</td><td></td><td>137.327</td><td>Barium</td><td>Ba</td><td>725</td><td>1140</td><td>3.59</td><td>0.05</td><td>1808</td><td>2</td><td>[Xe] 6s<sup>2</sup></td><td>5.2117</td></tr><tr><td>57</td><td></td><td>138.9055</td><td>Lanthanum</td><td>La</td><td>920</td><td>3469</td><td>6.15</td><td></td><td>1839</td><td>3</td><td>[Xe] 5d<sup>1</sup> 6s<sup>2</sup></td><td>5.5769</td></tr><tr class="bkgcyan"><td>58</td><td></td><td>140.116</td><td>Cerium</td><td>Ce</td><td>795</td><td>3257</td><td>6.77</td><td></td><td>1803</td><td>101</td><td>[Xe] 4f<sup>1</sup> 5d<sup>1</sup> 6s<sup>2</sup></td><td>5.5387</td></tr><tr><td>59</td><td></td><td>140.9077</td><td>Praseodymium</td><td>Pr</td><td>935</td><td>3127</td><td>6.77</td><td></td><td>1885</td><td>101</td><td>[Xe] 4f<sup>3</sup> 6s<sup>2</sup></td><td>5.473</td></tr><tr class="bkgcyan"><td>60</td><td></td><td>144.24</td><td>Neodymium</td><td>Nd</td><td>1010</td><td>3127</td><td>7.01</td><td></td><td>1885</td><td>101</td><td>[Xe] 4f<sup>4</sup> 6s<sup>2</sup></td><td>5.525</td></tr><tr><td>61</td><td>*</td><td>145</td><td>Promethium</td><td>Pm</td><td>1100</td><td>3000</td><td>7.3</td><td></td><td>1945</td><td>101</td><td>[Xe] 4f<sup>5</sup> 6s<sup>2</sup></td><td>5.582</td></tr><tr class="bkgcyan"><td>62</td><td></td><td>150.36</td><td>Samarium</td><td>Sm</td><td>1072</td><td>1900</td><td>7.52</td><td></td><td>1879</td><td>101</td><td>[Xe] 4f<sup>6</sup> 6s<sup>2</sup></td><td>5.6437</td></tr><tr><td>63</td><td></td><td>151.964</td><td>Europium</td><td>Eu</td><td>822</td><td>1597</td><td>5.24</td><td></td><td>1901</td><td>101</td><td>[Xe] 4f<sup>7</sup> 6s<sup>2</sup></td><td>5.6704</td></tr><tr class="bkgcyan"><td>64</td><td></td><td>157.25</td><td>Gadolinium</td><td>Gd</td><td>1311</td><td>3233</td><td>7.9</td><td></td><td>1880</td><td>101</td><td>[Xe] 4f<sup>7</sup> 5d<sup>1</sup> 6s<sup>2</sup></td><td>6.1501</td></tr><tr><td>65</td><td></td><td>158.9253</td><td>Terbium</td><td>Tb</td><td>1360</td><td>3041</td><td>8.23</td><td></td><td>1843</td><td>101</td><td>[Xe] 4f<sup>9</sup> 6s<sup>2</sup></td><td>5.8638</td></tr><tr class="bkgcyan"><td>66</td><td></td><td>162.5</td><td>Dysprosium</td><td>Dy</td><td>1412</td><td>2562</td><td>8.55</td><td></td><td>1886</td><td>101</td><td>[Xe] 4f<sup>10</sup> 6s<sup>2</sup></td><td>5.9389</td></tr><tr><td>67</td><td></td><td>164.9303</td><td>Holmium</td><td>Ho</td><td>1470</td><td>2720</td><td>8.8</td><td></td><td>1867</td><td>101</td><td>[Xe] 4f<sup>11</sup> 6s<sup>2</sup></td><td>6.0215</td></tr><tr class="bkgcyan"><td>68</td><td></td><td>167.259</td><td>Erbium</td><td>Er</td><td>1522</td><td>2510</td><td>9.07</td><td></td><td>1842</td><td>101</td><td>[Xe] 4f<sup>12</sup> 6s<sup>2</sup></td><td>6.1077</td></tr><tr><td>69</td><td></td><td>168.9342</td><td>Thulium</td><td>Tm</td><td>1545</td><td>1727</td><td>9.32</td><td></td><td>1879</td><td>101</td><td>[Xe] 4f<sup>13</sup> 6s<sup>2</sup></td><td>6.1843</td></tr><tr class="bkgcyan"><td>70</td><td></td><td>173.04</td><td>Ytterbium</td><td>Yb</td><td>824</td><td>1466</td><td>6.9</td><td></td><td>1878</td><td>101</td><td>[Xe] 4f<sup>14</sup> 6s<sup>2</sup></td><td>6.2542</td></tr><tr><td>71</td><td></td><td>174.967</td><td>Lutetium</td><td>Lu</td><td>1656</td><td>3315</td><td>9.84</td><td></td><td>1907</td><td>101</td><td>[Xe] 4f<sup>14</sup> 5d<sup>1</sup> 6s<sup>2</sup></td><td>5.4259</td></tr><tr class="bkgcyan"><td>72</td><td></td><td>178.49</td><td>Hafnium</td><td>Hf</td><td>2150</td><td>5400</td><td>13.31</td><td></td><td>1923</td><td>4</td><td>[Xe] 4f<sup>14</sup> 5d<sup>2</sup> 6s<sup>2</sup></td><td>6.8251</td></tr><tr><td>73</td><td></td><td>180.9479</td><td>Tantalum</td><td>Ta</td><td>2996</td><td>5425</td><td>16.65</td><td></td><td>1802</td><td>5</td><td>[Xe] 4f<sup>14</sup> 5d<sup>3</sup> 6s<sup>2</sup></td><td>7.5496</td></tr><tr class="bkgcyan"><td>74</td><td></td><td>183.84</td><td>Tungsten</td><td>W</td><td>3410</td><td>5660</td><td>19.35</td><td></td><td>1783</td><td>6</td><td>[Xe] 4f<sup>14</sup> 5d<sup>4</sup> 6s<sup>2</sup></td><td>7.864</td></tr><tr><td>75</td><td></td><td>186.207</td><td>Rhenium</td><td>Re</td><td>3180</td><td>5627</td><td>21.04</td><td></td><td>1925</td><td>7</td><td>[Xe] 4f<sup>14</sup> 5d<sup>5</sup> 6s<sup>2</sup></td><td>7.8335</td></tr><tr class="bkgcyan"><td>76</td><td></td><td>190.23</td><td>Osmium</td><td>Os</td><td>3045</td><td>5027</td><td>22.6</td><td></td><td>1803</td><td>8</td><td>[Xe] 4f<sup>14</sup> 5d<sup>6</sup> 6s<sup>2</sup></td><td>8.4382</td></tr><tr><td>77</td><td></td><td>192.217</td><td>Iridium</td><td>Ir</td><td>2410</td><td>4527</td><td>22.4</td><td></td><td>1803</td><td>9</td><td>[Xe] 4f<sup>14</sup> 5d<sup>7</sup> 6s<sup>2</sup></td><td>8.967</td></tr><tr class="bkgcyan"><td>78</td><td></td><td>195.078</td><td>Platinum</td><td>Pt</td><td>1772</td><td>3827</td><td>21.45</td><td></td><td>1735</td><td>10</td><td>[Xe] 4f<sup>14</sup> 5d<sup>9</sup> 6s<sup>1</sup></td><td>8.9587</td></tr><tr><td>79</td><td></td><td>196.9665</td><td>Gold</td><td>Au</td><td>1064</td><td>2807</td><td>19.32</td><td></td><td> ancient</td><td>11</td><td>[Xe] 4f<sup>14</sup> 5d<sup>10</sup> 6s<sup>1</sup></td><td>9.2255</td></tr><tr class="bkgcyan"><td>80</td><td></td><td>200.59</td><td>Mercury</td><td>Hg</td><td>-39</td><td>357</td><td>13.55</td><td></td><td> ancient</td><td>12</td><td>[Xe] 4f<sup>14</sup> 5d<sup>10</sup> 6s<sup>2</sup></td><td>10.4375</td></tr><tr><td>81</td><td></td><td>204.3833</td><td>Thallium</td><td>Tl</td><td>303</td><td>1457</td><td>11.85</td><td></td><td>1861</td><td>13</td><td>[Xe] 4f<sup>14</sup> 5d<sup>10</sup> 6s<sup>2</sup> 6p<sup>1</sup></td><td>6.1082</td></tr><tr class="bkgcyan"><td>82</td><td></td><td>207.2</td><td>Lead</td><td>Pb</td><td>327</td><td>1740</td><td>11.35</td><td></td><td> ancient</td><td>14</td><td>[Xe] 4f<sup>14</sup> 5d<sup>10</sup> 6s<sup>2</sup> 6p<sup>2</sup></td><td>7.4167</td></tr><tr><td>83</td><td></td><td>208.9804</td><td>Bismuth</td><td>Bi</td><td>271</td><td>1560</td><td>9.75</td><td></td><td> ancient</td><td>15</td><td>[Xe] 4f<sup>14</sup> 5d<sup>10</sup> 6s<sup>2</sup> 6p<sup>3</sup></td><td>7.2856</td></tr><tr class="bkgcyan"><td>84</td><td>*</td><td>209</td><td>Polonium</td><td>Po</td><td>254</td><td>962</td><td>9.3</td><td></td><td>1898</td><td>16</td><td>[Xe] 4f<sup>14</sup> 5d<sup>10</sup> 6s<sup>2</sup> 6p<sup>4</sup></td><td>8.417</td></tr><tr><td>85</td><td>*</td><td>210</td><td>Astatine</td><td>At</td><td>302</td><td>337</td><td></td><td></td><td>1940</td><td>17</td><td>[Xe] 4f<sup>14</sup> 5d<sup>10</sup> 6s<sup>2</sup> 6p<sup>5</sup></td><td>9.3</td></tr><tr class="bkgcyan"><td>86</td><td>*</td><td>222</td><td>Radon</td><td>Rn</td><td>-71</td><td>-62</td><td>9.73</td><td></td><td>1900</td><td>18</td><td>[Xe] 4f<sup>14</sup> 5d<sup>10</sup> 6s<sup>2</sup> 6p<sup>6</sup></td><td>10.7485</td></tr><tr><td>87</td><td>*</td><td>223</td><td>Francium</td><td>Fr</td><td>27</td><td>677</td><td></td><td></td><td>1939</td><td>1</td><td>[Rn] 7s<sup>1</sup></td><td>4.0727</td></tr><tr class="bkgcyan"><td>88</td><td>*</td><td>226</td><td>Radium</td><td>Ra</td><td>700</td><td>1737</td><td>5.5</td><td></td><td>1898</td><td>2</td><td>[Rn] 7s<sup>2</sup></td><td>5.2784</td></tr><tr><td>89</td><td>*</td><td>227</td><td>Actinium</td><td>Ac</td><td>1050</td><td>3200</td><td>10.07</td><td></td><td>1899</td><td>3</td><td>[Rn] 6d<sup>1</sup> 7s<sup>2</sup></td><td>5.17</td></tr><tr class="bkgcyan"><td>90</td><td></td><td>232.0381</td><td>Thorium</td><td>Th</td><td>1750</td><td>4790</td><td>11.72</td><td></td><td>1829</td><td>102</td><td>[Rn] 6d<sup>2</sup> 7s<sup>2</sup></td><td>6.3067</td></tr><tr><td>91</td><td></td><td>231.0359</td><td>Protactinium</td><td>Pa</td><td>1568</td><td></td><td>15.4</td><td></td><td>1913</td><td>102</td><td>[Rn] 5f<sup>2</sup> 6d<sup>1</sup> 7s<sup>2</sup></td><td>5.89</td></tr><tr class="bkgcyan"><td>92</td><td></td><td>238.0289</td><td>Uranium</td><td>U</td><td>1132</td><td>3818</td><td>18.95</td><td></td><td>1789</td><td>102</td><td>[Rn] 5f<sup>3</sup> 6d<sup>1</sup> 7s<sup>2</sup></td><td>6.1941</td></tr><tr><td>93</td><td>*</td><td>237</td><td>Neptunium</td><td>Np</td><td>640</td><td>3902</td><td>20.2</td><td></td><td>1940</td><td>102</td><td>[Rn] 5f<sup>4</sup> 6d<sup>1</sup> 7s<sup>2</sup></td><td>6.2657</td></tr><tr class="bkgcyan"><td>94</td><td>*</td><td>244</td><td>Plutonium</td><td>Pu</td><td>640</td><td>3235</td><td>19.84</td><td></td><td>1940</td><td>102</td><td>[Rn] 5f<sup>6</sup> 7s<sup>2</sup></td><td>6.0262</td></tr><tr><td>95</td><td>*</td><td>243</td><td>Americium</td><td>Am</td><td>994</td><td>2607</td><td>13.67</td><td></td><td>1944</td><td>102</td><td>[Rn] 5f<sup>7</sup> 7s<sup>2</sup></td><td>5.9738</td></tr><tr class="bkgcyan"><td>96</td><td>*</td><td>247</td><td>Curium</td><td>Cm</td><td>1340</td><td></td><td>13.5</td><td></td><td>1944</td><td>102</td><td></td><td>5.9915</td></tr><tr><td>97</td><td>*</td><td>247</td><td>Berkelium</td><td>Bk</td><td>986</td><td></td><td>14.78</td><td></td><td>1949</td><td>102</td><td></td><td>6.1979</td></tr><tr class="bkgcyan"><td>98</td><td>*</td><td>251</td><td>Californium</td><td>Cf</td><td>900</td><td></td><td>15.1</td><td></td><td>1950</td><td>102</td><td></td><td>6.2817</td></tr><tr><td>99</td><td>*</td><td>252</td><td>Einsteinium</td><td>Es</td><td>860</td><td></td><td></td><td></td><td>1952</td><td>102</td><td></td><td>6.42</td></tr><tr class="bkgcyan"><td>100</td><td>*</td><td>257</td><td>Fermium</td><td>Fm</td><td>1527</td><td></td><td></td><td></td><td>1952</td><td>102</td><td></td><td>6.5</td></tr><tr><td>101</td><td>*</td><td>258</td><td>Mendelevium</td><td>Md</td><td></td><td></td><td></td><td></td><td>1955</td><td>102</td><td></td><td>6.58</td></tr><tr class="bkgcyan"><td>102</td><td>*</td><td>259</td><td>Nobelium</td><td>No</td><td>827</td><td></td><td></td><td></td><td>1958</td><td>102</td><td></td><td>6.65</td></tr><tr><td>103</td><td>*</td><td>262</td><td>Lawrencium</td><td>Lr</td><td>1627</td><td></td><td></td><td></td><td>1961</td><td>102</td><td></td><td>4.9</td></tr><tr class="bkgcyan"><td>104</td><td>*</td><td>261</td><td>Rutherfordium</td><td>Rf</td><td></td><td></td><td></td><td></td><td>1964</td><td>4</td><td></td><td></td></tr><tr><td>105</td><td>*</td><td>262</td><td>Dubnium</td><td>Db</td><td></td><td></td><td></td><td></td><td>1967</td><td>5</td><td></td><td></td></tr><tr class="bkgcyan"><td>106</td><td>*</td><td>266</td><td>Seaborgium</td><td>Sg</td><td></td><td></td><td></td><td></td><td>1974</td><td>6</td><td></td><td></td></tr><tr><td>107</td><td>*</td><td>264</td><td>Bohrium</td><td>Bh</td><td></td><td></td><td></td><td></td><td>1981</td><td>7</td><td></td><td></td></tr><tr class="bkgcyan"><td>108</td><td>*</td><td>277</td><td>Hassium</td><td>Hs</td><td></td><td></td><td></td><td></td><td>1984</td><td>8</td><td></td><td></td></tr><tr><td>109</td><td>*</td><td>268</td><td>Meitnerium</td><td>Mt</td><td></td><td></td><td></td><td></td><td>1982</td><td>9</td><td></td><td></td></tr>
#"""
 #   elementSearch=re.compile(r'<tr(?: class="bkgcyan")?><td>(?P<atomNumber>[0-9]{1,3})</td><td>(?P<unstable>[*]?)</td><td>(?P<atomWeight>[\d.]*)</td><td>(?P<atomName>[^<]+)</td><td>(?P<atomSymbol>[a-zA-Z]{1,2})</td><td>(?P<meltPointCelc>[-0-9.]*)</td><td>(?P<boilPointCelc>[-0-9.]*)</td><td>(?P<density>[^<]*)</td><td>[^<]*</td><td>[^<]*</td><td>(?P<group>[0-9]{1,3})</td><td>(?P<electronConfig>(?:[^<]*(?:<sup>[^<]*</sup>))*)</td><td>(?P<firstIonizationEnergy>[-0-9.]*)</td></tr>')
 #   test=elementSearch.findall(periodicTable)
