import blosum as bl
import numpy as np

matrix = bl.BLOSUM("Ej_Algo_2/blosum40.file")

def test_symmetrical_matrix(matrix):

    aminoacids="ARNDCQEGHILKMFPSTWYVBZX"

    for l1 in aminoacids:
        for l2 in aminoacids:
            if matrix[l1][l2]!=matrix[l2][l1]:
                raise ValueError("La matriz no es simétrica")
            
test_symmetrical_matrix(matrix)
            
def Needleman_Wunsch(seq1, seq2, matrix):
    seq1,seq2="0"+seq1,"0"+seq2
    table=np.zeros((len(seq1),len(seq2)),dtype=np.int16)
    numtable=np.zeros((len(seq1),len(seq2)),dtype=np.int16)

    for f1 in range(1,len(seq1)):
        table[f1,0]=f1*-8
        numtable[f1,0]=2

    for f2 in range(1,len(seq2)):
        table[0,f2]=f2*-8
        numtable[0,f2]=3

    for l1 in range(1,len(seq1)):
        for l2 in range(1,len(seq2)):
            option1=table[l1-1,l2-1]+matrix[seq1[l1]][seq2[l2]]
            option2=table[l1-1,l2]-8
            option3=table[l1,l2-1]-8
            if max(option1, option2, option3)==option1:
                table[l1,l2]=option1
                numtable[l1,l2]=1
            elif max(option1, option2, option3)==option2:
                table[l1,l2]=option2
                numtable[l1,l2]=2
            elif max(option1, option2, option3)==option3:
                table[l1,l2]=option3
                numtable[l1,l2]=3
                             
    return table,np.matrix(numtable)

# print(Needleman_Wunsch("KTEAEMKASEDLKKHGT","HGSAQVKGHG", matrix)[0])

# print(Needleman_Wunsch("KTEAEMKASEDLKKHGT","HGSAQVKGHG", matrix)[1])


def buildalignment(seq1,seq2,matrix,result:list[list[str]]=[[],[]]):
    option=matrix[len(seq1), len(seq2)]
    if option == 1:
        result[0].insert(0,seq1[-1])
        result[1].insert(0,seq2[-1])
        seq1=seq1[:-1]
        seq2=seq2[:-1]
        matrix=matrix[:-1,:-1]
        buildalignment(seq1,seq2,matrix,result)


    elif option == 2:
        result[0].insert(0,seq1[-1])
        result[1].insert(0,"-")
        seq1=seq1[:-1]
        matrix=matrix[:-1]
        buildalignment(seq1,seq2,matrix,result)


    elif option == 3:
        result[0].insert(0,"-")
        result[1].insert(0,seq2[-1])
        seq2=seq2[:-1]
        matrix=matrix[:,:-1]
        buildalignment(seq1,seq2,matrix,result)

    
    return "".join(result[0])+"\n"+"".join(result[1])

def similarity_score(seq1,seq2):
    matches, mismatches = 0, 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            matches+=1
        else:
            mismatches+=1
    return mismatches/matches

sequences=["PPGVKSDCAS","PADGVKDCAS","PPDGKSDS","GADGKDCCS","GADGKDCAS"]


for i in range(len(sequences)):
    for j in range(i+1,len(sequences)):
        if i!=j:
            print(f"\nFor sequences: {sequences[i]} and {sequences[j]}")
            NW=Needleman_Wunsch(sequences[i],sequences[j],matrix)
            Al=buildalignment(sequences[i],sequences[j],NW[1], result=[[],[]])
            print(Al + "\n")
            
            print(similarity_score(Al.split("\n")[0],Al.split("\n")[1]))