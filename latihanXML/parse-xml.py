import xml.dom.minidom as minidom

def main():
    
    doc = minidom.parse("D:\E\Kuliah Haya\semester 4\mesin\latihanXML\mahasiswa.xml")

    print(doc.nodeName)
    print(doc.firstChild.tagName)


    nama = doc.getElementsByTagName("nama")[0].firstChild.data
    alamat = doc.getElementsByTagName("alamat")[0].firstChild.data
    jurusan = doc.getElementsByTagName("jurusan")[0].firstChild.data
    list_hobi = doc.getElementsByTagName("hobi")

    print ("\nNama: {}\nAlamat: {}\nJurusan: {}\n".format(nama, alamat, jurusan))

    print ("Memiliki {} hobi:".format(len(list_hobi)))

    for hobi in list_hobi:
        print ("-", hobi.getAttribute("name"))

    nama = doc.getElementsByTagName("nama")[1].firstChild.data
    alamat = doc.getElementsByTagName("alamat")[1].firstChild.data
    jurusan = doc.getElementsByTagName("jurusan")[1].firstChild.data
    list_hobi = doc.getElementsByTagName("hobi")

    
    print ("\nNama: {}\nAlamat: {}\nJurusan: {}\n".format(nama, alamat, jurusan))

    print ("Memiliki {} hobi:".format(len(list_hobi)))

    for hobi in list_hobi:
        print ("-", hobi.getAttribute("name"))


if __name__ == "__main__":
    main()