import tkinter as tk
import random as rn

def generer_tekst():
    knapp.destroy()
    navn = ["Aya, ", "Annabelle, ", "Celine, ", "Hanna, ", "Hedda, ", "Isabella, ", "Nadia, ", "Mats, ", "Sara, ", "Synnøve, ", "Ulrikke, ", "Line, ", "Ole Fridtjof, ", "Eva Kristin, ", "Randi, ", "Anette, "]
    del1 = ["som lærer synes jeg du er ", "du er ", "det fremstår som at du er ", "som elev er du ", "jeg er glad for at du er ", "i undervisningen er du "]
    del2 = ["en gang i blant ", "innimellom ", "hjelpsom og ", "åpenbart ", "super ", "mest sannsynlig ", "meget ", "veldig ", "", "sinnsykt ", "flink i å være ", "fortsatt ", "omsorgsfull og "]
    del3 = ["våken i timen", "støttende", "forståelsesfull", "oppmuntrende", "fornøyd", "inspirerende", "arbeidsom", "oppegående", "til stede", "god medelev", "smart", "tilgivende", "trygg", "empatisk", "klok", "lur", "eksisterende"]
    del4 = ["!", "?", ".", "", "!?", "?!", "!!!", "!!!!!"]
    tekst.delete(0, "end")
    n = len(navn) - 1
    r = rn.randint(0, n)
    l1 = len(del1) - 1
    r1 = rn.randint(0, l1)
    l2 = len(del2) - 1
    r2 = rn.randint(0, l2)
    l3 = len(del3) - 1
    r3 = rn.randint(0, l3)
    l4 = len(del4) - 1
    r4 = rn.randint(0, l4)
    text = f"{navn[r]}{del1[r1]}{del2[r2]}{del3[r3]}{del4[r4]}"
    tekst.insert(0, text)
    root.after(10000, generer_tekst)

root = tk.Tk()

tekst = tk.Entry(root, width = 70, font = ("Arial", 30))
tekst.pack()

knapp = tk.Button(root, text = "Trykk her!", font = ("Arial", 20), command = generer_tekst)
knapp.pack()

root.mainloop()