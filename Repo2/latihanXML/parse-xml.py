import xml.dom.minidom as minidom

def main():
    
    doc = minidom.parse(r"D:\E\Kuliah Haya\semester 4\mesin\latihanXML\karakter.xml")

    print(doc.nodeName)
    print("Karakter Initia D\n")

    no = doc.getElementsByTagName("no")[0].firstChild.data
    nama = doc.getElementsByTagName("nama")[0].firstChild.data
    kendaraan = doc.getElementsByTagName("kendaraan")[0].firstChild.data
    asal = doc.getElementsByTagName("asal")[0].firstChild.data
    status = doc.getElementsByTagName("status")[0].firstChild.data

    print ("\nNo: {} \nNama: {}\nKendaraan: {}\nAsal: {}\nStatus: {}".format(no, nama, kendaraan, asal, status))

    no = doc.getElementsByTagName("no")[1].firstChild.data
    nama = doc.getElementsByTagName("nama")[1].firstChild.data
    kendaraan = doc.getElementsByTagName("kendaraan")[1].firstChild.data
    asal = doc.getElementsByTagName("asal")[1].firstChild.data
    status = doc.getElementsByTagName("status")[1].firstChild.data

    print ("\nNo: {} \nNama: {}\nKendaraan: {}\nAsal: {}\nStatus: {}".format(no, nama, kendaraan, asal, status))

    no = doc.getElementsByTagName("no")[2].firstChild.data
    nama = doc.getElementsByTagName("nama")[2].firstChild.data
    kendaraan = doc.getElementsByTagName("kendaraan")[2].firstChild.data
    asal = doc.getElementsByTagName("asal")[2].firstChild.data
    status = doc.getElementsByTagName("status")[2].firstChild.data

    print ("\nNo: {} \nNama: {}\nKendaraan: {}\nAsal: {}\nStatus: {}".format(no, nama, kendaraan, asal, status))

    no = doc.getElementsByTagName("no")[3].firstChild.data
    nama = doc.getElementsByTagName("nama")[3].firstChild.data
    kendaraan = doc.getElementsByTagName("kendaraan")[3].firstChild.data
    asal = doc.getElementsByTagName("asal")[3].firstChild.data
    status = doc.getElementsByTagName("status")[3].firstChild.data

    print ("\nNo: {} \nNama: {}\nKendaraan: {}\nAsal: {}\nStatus: {}".format(no, nama, kendaraan, asal, status))

    no = doc.getElementsByTagName("no")[4].firstChild.data
    nama = doc.getElementsByTagName("nama")[4].firstChild.data
    kendaraan = doc.getElementsByTagName("kendaraan")[4].firstChild.data
    asal = doc.getElementsByTagName("asal")[4].firstChild.data
    status = doc.getElementsByTagName("status")[4].firstChild.data

    print ("\nNo: {} \nNama: {}\nKendaraan: {}\nAsal: {}\nStatus: {}".format(no, nama, kendaraan, asal, status))

    no = doc.getElementsByTagName("no")[5].firstChild.data
    nama = doc.getElementsByTagName("nama")[5].firstChild.data
    kendaraan = doc.getElementsByTagName("kendaraan")[5].firstChild.data
    asal = doc.getElementsByTagName("asal")[5].firstChild.data
    status = doc.getElementsByTagName("status")[5].firstChild.data

    print ("\nNo: {} \nNama: {}\nKendaraan: {}\nAsal: {}\nStatus: {}".format(no, nama, kendaraan, asal, status))

    no = doc.getElementsByTagName("no")[6].firstChild.data
    nama = doc.getElementsByTagName("nama")[6].firstChild.data
    kendaraan = doc.getElementsByTagName("kendaraan")[6].firstChild.data
    asal = doc.getElementsByTagName("asal")[6].firstChild.data
    status = doc.getElementsByTagName("status")[6].firstChild.data

    print ("\nNo: {} \nNama: {}\nKendaraan: {}\nAsal: {}\nStatus: {}".format(no, nama, kendaraan, asal, status))

    no = doc.getElementsByTagName("no")[7].firstChild.data
    nama = doc.getElementsByTagName("nama")[7].firstChild.data
    kendaraan = doc.getElementsByTagName("kendaraan")[7].firstChild.data
    asal = doc.getElementsByTagName("asal")[7].firstChild.data
    status = doc.getElementsByTagName("status")[7].firstChild.data

    print ("\nNo: {} \nNama: {}\nKendaraan: {}\nAsal: {}\nStatus: {}".format(no, nama, kendaraan, asal, status))

    no = doc.getElementsByTagName("no")[8].firstChild.data
    nama = doc.getElementsByTagName("nama")[8].firstChild.data
    kendaraan = doc.getElementsByTagName("kendaraan")[8].firstChild.data
    asal = doc.getElementsByTagName("asal")[8].firstChild.data
    status = doc.getElementsByTagName("status")[8].firstChild.data

    print ("\nNo: {} \nNama: {}\nKendaraan: {}\nAsal: {}\nStatus: {}".format(no, nama, kendaraan, asal, status))

    no = doc.getElementsByTagName("no")[9].firstChild.data
    nama = doc.getElementsByTagName("nama")[9].firstChild.data
    kendaraan = doc.getElementsByTagName("kendaraan")[9].firstChild.data
    asal = doc.getElementsByTagName("asal")[9].firstChild.data
    status = doc.getElementsByTagName("status")[9].firstChild.data

    print ("\nNo: {} \nNama: {}\nKendaraan: {}\nAsal: {}\nStatus: {}\n".format(no, nama, kendaraan, asal, status))  

if __name__ == "__main__":
    main()