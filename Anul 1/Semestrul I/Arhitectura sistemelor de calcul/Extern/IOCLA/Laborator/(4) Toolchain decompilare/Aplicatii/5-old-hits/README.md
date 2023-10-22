# Writeup

Exercițiul necesită găsirea unei valori generate random în main folosind `gdb`
pentru extragerea datelor, și ghidra pentru înțelegerea codului (este făcut să
fie rezolvat înainte de laboratoarele de limbaj de asamblare).

În urma rezolvării, codul afișează un link către un video ales aleator dintr-o
listă. Lista de linkuri criptată și codificată în base64 este ținută în
variabila `enc_b64`, iar lista de linkuri în variabila `links`.

Lista plain text este definită doar dacă macro-ul `REENCRYPT` este definit.
Pentru rezolvarea exercițiilor, macro-ul nu este definit, iar lista nu este
vizibilă.
