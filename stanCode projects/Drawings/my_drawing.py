"""
File: my_drawing.py
Name:Thomas
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Olaf!

    I feel exhausted after drawing this with 600 lines of code.
    But is cute.
    """
    window = GWindow(1500, 1500, title="Olaf")
    background = GRect(1500, 1500)
    background.filled = True
    background.fill_color = "lightskyblue"
    window.add(background)

    bg2 = GPolygon()
    bg2.add_vertex((1350, 688))
    bg2.add_vertex((1355, 597))
    bg2.add_vertex((1290, 566))
    bg2.add_vertex((1219, 594))
    bg2.add_vertex((1232, 709))
    bg2.add_vertex((1092, 628))
    bg2.add_vertex((1195, 583))
    bg2.add_vertex((1189, 509))
    bg2.add_vertex((1129, 468))
    bg2.add_vertex((1049, 517))
    bg2.add_vertex((1047, 414))
    bg2.add_vertex((1249, 285))
    bg2.add_vertex((1266, 193))
    bg2.add_vertex((1196, 171))
    bg2.add_vertex((1049, 275))
    bg2.add_vertex((1047, 53))
    bg2.add_vertex((980, 26))
    bg2.add_vertex((920, 54))
    bg2.add_vertex((911, 273))
    bg2.add_vertex((762, 178))
    bg2.add_vertex((692, 195))
    bg2.add_vertex((711, 284))
    bg2.add_vertex((914, 409))
    bg2.add_vertex((910, 516))
    bg2.add_vertex((832, 468))
    bg2.add_vertex((774, 512))
    bg2.add_vertex((764, 584))
    bg2.add_vertex((871, 626))
    bg2.add_vertex((723, 711))
    bg2.add_vertex((744, 594))
    bg2.add_vertex((679, 567))
    bg2.add_vertex((607, 594))
    bg2.add_vertex((611, 688))
    bg2.add_vertex((523, 636))
    bg2.add_vertex((507, 402))
    bg2.add_vertex((443, 341))
    bg2.add_vertex((383, 393))
    bg2.add_vertex((400, 569))
    bg2.add_vertex((211, 459))
    bg2.add_vertex((150, 506))
    bg2.add_vertex((142, 571))
    bg2.add_vertex((332, 687))
    bg2.add_vertex((173, 764))
    bg2.add_vertex((159, 827))
    bg2.add_vertex((240, 866))
    bg2.add_vertex((452, 763))
    bg2.add_vertex((541, 807))
    bg2.add_vertex((456, 853))
    bg2.add_vertex((466, 926))
    bg2.add_vertex((525, 972))
    bg2.add_vertex((619, 901))
    bg2.add_vertex((617, 1068))
    bg2.add_vertex((525, 1001))
    bg2.add_vertex((466, 1041))
    bg2.add_vertex((456, 1111))
    bg2.add_vertex((544, 1162))
    bg2.add_vertex((451, 1208))
    bg2.add_vertex((239, 1104))
    bg2.add_vertex((163, 1131))
    bg2.add_vertex((164, 1202))
    bg2.add_vertex((331, 1283))
    bg2.add_vertex((144, 1391))
    bg2.add_vertex((147, 1485))
    bg2.add_vertex((203, 1503))
    bg2.add_vertex((407, 1401))
    bg2.add_vertex((387, 1500))
    bg2.add_vertex((512, 1500))
    bg2.add_vertex((518, 1327))
    bg2.add_vertex((610, 1279))
    bg2.add_vertex((608, 1369))
    bg2.add_vertex((674, 1399))
    bg2.add_vertex((740, 1371))
    bg2.add_vertex((725, 1260))
    bg2.add_vertex((888, 1339))
    bg2.add_vertex((766, 1384))
    bg2.add_vertex((770, 1456))
    bg2.add_vertex((830, 1501))
    bg2.add_vertex((910, 1450))
    bg2.add_vertex((911, 1500))
    bg2.add_vertex((1046, 1500))
    bg2.add_vertex((1129, 1497))
    bg2.add_vertex((1130, 1500))
    bg2.add_vertex((1189, 1452))
    bg2.add_vertex((1196, 1387))
    bg2.add_vertex((1091, 1342))
    bg2.add_vertex((1232, 1261))
    bg2.add_vertex((1219, 1371))
    bg2.add_vertex((1286, 1399))
    bg2.add_vertex((1352, 1368))
    bg2.add_vertex((1348, 1276))
    bg2.add_vertex((1439, 1327))
    bg2.add_vertex((1448, 1500))
    bg2.add_vertex((1500, 1500))
    bg2.add_vertex((1500, 1210))
    bg2.add_vertex((1421, 1162))
    bg2.add_vertex((1500, 1114))
    bg2.add_vertex((1490, 1041))
    bg2.add_vertex((1435, 1000))
    bg2.add_vertex((1343, 1065))
    bg2.add_vertex((1343, 901))
    bg2.add_vertex((1435, 970))
    bg2.add_vertex((1495, 925))
    bg2.add_vertex((1500, 856))
    bg2.add_vertex((1420, 813))
    bg2.add_vertex((1500, 762))
    bg2.add_vertex((1500, 345))
    bg2.add_vertex((1451, 403))
    bg2.add_vertex((1441, 639))
    bg2.filled = True
    bg2.fill_color = "blue"
    bg2.color = "blue"
    window.add(bg2)

    bg1 = GPolygon()
    bg1.add_vertex((721, 835))
    bg1.add_vertex((980, 684))
    bg1.add_vertex((1243, 835))
    bg1.add_vertex((1240, 1136))
    bg1.add_vertex((978, 1287))
    bg1.add_vertex((722, 1135))
    bg1.filled = True
    bg1.fill_color = "lightskyblue"
    bg1.color = "lightskyblue"
    window.add(bg1)

    hair1 = GPolygon()
    hair1.add_vertex((888, 291))
    hair1.add_vertex((891, 280))
    hair1.add_vertex((915, 214))
    hair1.add_vertex((898, 172))
    hair1.add_vertex((863, 148))
    hair1.add_vertex((844, 156))
    hair1.add_vertex((839, 151))
    hair1.add_vertex((864, 142))
    hair1.add_vertex((896, 162))
    hair1.add_vertex((916, 199))
    hair1.add_vertex((916, 179))
    hair1.add_vertex((921, 174))
    hair1.add_vertex((917, 139))
    hair1.add_vertex((924, 137))
    hair1.add_vertex((925, 175))
    hair1.add_vertex((922, 183))
    hair1.add_vertex((920, 198))
    hair1.add_vertex((918, 245))
    hair1.add_vertex((897, 282))
    hair1.add_vertex((891, 292))
    hair1.filled = True
    hair1.fill_color = "black"
    hair1.color = "black"
    window.add(hair1)

    hair2 = GPolygon()
    hair2.add_vertex((898, 297))
    hair2.add_vertex((905, 285))
    hair2.add_vertex((924, 248))
    hair2.add_vertex((945, 198))
    hair2.add_vertex((950, 142))
    hair2.add_vertex((948, 87))
    hair2.add_vertex((940, 80))
    hair2.add_vertex((946, 78))
    hair2.add_vertex((924, 33))
    hair2.add_vertex((927, 31))
    hair2.add_vertex((947, 64))
    hair2.add_vertex((956, 123))
    hair2.add_vertex((955, 172))
    hair2.add_vertex((953, 192))
    hair2.add_vertex((935, 245))
    hair2.add_vertex((910, 285))
    hair2.add_vertex((902, 300))
    hair2.filled = True
    hair2.fill_color = "black"
    hair2.color = "black"
    window.add(hair2)

    hair3 = GPolygon()
    hair3.add_vertex((905, 302))
    hair3.add_vertex((937, 258))
    hair3.add_vertex((940, 255))
    hair3.add_vertex((997, 191))
    hair3.add_vertex((1005, 173))
    hair3.add_vertex((1003, 187))
    hair3.add_vertex((1038, 174))
    hair3.add_vertex((1055, 180))
    hair3.add_vertex((1065, 194))
    hair3.add_vertex((1053, 185))
    hair3.add_vertex((1041, 181))
    hair3.add_vertex((1014, 191))
    hair3.add_vertex((967, 228))
    hair3.add_vertex((945, 261))
    hair3.add_vertex((921, 293))
    hair3.add_vertex((910, 308))
    hair3.filled = True
    hair3.fill_color = "black"
    hair3.color = "black"
    window.add(hair3)

    rarm = GPolygon()
    rarm.add_vertex((755, 812))
    rarm.add_vertex((798, 796))
    rarm.add_vertex((858, 780))
    rarm.add_vertex((873, 762))
    rarm.add_vertex((907, 747))
    rarm.add_vertex((934, 727))
    rarm.add_vertex((973, 707))
    rarm.add_vertex((991, 687))
    rarm.add_vertex((1016, 670))
    rarm.add_vertex((1009, 645))
    rarm.add_vertex((1013, 635))
    rarm.add_vertex((1026, 657))
    rarm.add_vertex((1045, 628))
    rarm.add_vertex((1060, 576))
    rarm.add_vertex((1072, 584))
    rarm.add_vertex((1064, 627))
    rarm.add_vertex((1102, 605))
    rarm.add_vertex((1111, 617))
    rarm.add_vertex((1075, 637))
    rarm.add_vertex((1115, 642))
    rarm.add_vertex((1113, 653))
    rarm.add_vertex((1070, 656))
    rarm.add_vertex((1033, 673))
    rarm.add_vertex((1016, 697))
    rarm.add_vertex((977, 717))
    rarm.add_vertex((951, 740))
    rarm.add_vertex((926, 761))
    rarm.add_vertex((896, 771))
    rarm.add_vertex((866, 797))
    rarm.add_vertex((844, 804))
    rarm.add_vertex((826, 824))
    rarm.add_vertex((804, 833))
    rarm.filled = True
    rarm.fill_color = "saddlebrown"
    rarm.color = "saddlebrown"
    window.add(rarm)

    larm = GPolygon()
    larm.add_vertex((609, 825))
    larm.add_vertex((590, 810))
    larm.add_vertex((543, 757))
    larm.add_vertex((498, 711))
    larm.add_vertex((505, 681))
    larm.add_vertex((488, 696))
    larm.add_vertex((458, 654))
    larm.add_vertex((436, 606))
    larm.add_vertex((459, 580))
    larm.add_vertex((449, 568))
    larm.add_vertex((432, 583))
    larm.add_vertex((434, 554))
    larm.add_vertex((455, 502))
    larm.add_vertex((435, 498))
    larm.add_vertex((425, 548))
    larm.add_vertex((410, 537))
    larm.add_vertex((402, 499))
    larm.add_vertex((382, 506))
    larm.add_vertex((398, 547))
    larm.add_vertex((361, 526))
    larm.add_vertex((356, 537))
    larm.add_vertex((396, 567))
    larm.add_vertex((418, 628))
    larm.add_vertex((455, 676))
    larm.add_vertex((486, 734))
    larm.add_vertex((535, 778))
    larm.add_vertex((573, 839))
    larm.add_vertex((582, 873))
    larm.filled = True
    larm.fill_color = "saddlebrown"
    larm.color = "saddlebrown"
    window.add(larm)

    body1 = GOval(280, 230, x=560, y=780)
    body1.filled = True
    body1.fill_color = "snow"
    body1.color = "snow"
    window.add(body1)

    body2 = GOval(350, 400, x=600, y=870)
    body2.filled = True
    body2.fill_color = "snow"
    body2.color = "snow"
    window.add(body2)

    body3 = GOval(400, 350, x=680, y=840)
    body3.filled = True
    body3.fill_color = "snow"
    body3.color = "snow"
    window.add(body3)

    head1 = GPolygon()
    head1.add_vertex((836, 267))
    head1.add_vertex((733, 356))
    head1.add_vertex((694, 357))
    head1.add_vertex((661, 395))
    head1.add_vertex((632, 502))
    head1.add_vertex((616, 646))
    head1.add_vertex((632, 800))
    head1.add_vertex((773, 800))
    head1.add_vertex((957, 619))
    head1.add_vertex((996, 542))
    head1.add_vertex((995, 516))
    head1.add_vertex((969, 486))
    head1.add_vertex((971, 342))
    head1.add_vertex((911, 292))
    head1.filled = True
    head1.fill_color = "snow"
    head1.color = "snow"
    window.add(head1)

    feet1 = GPolygon()
    feet1.add_vertex((717, 1262))
    feet1.add_vertex((702, 1287))
    feet1.add_vertex((694, 1317))
    feet1.add_vertex((710, 1354))
    feet1.add_vertex((753, 1368))
    feet1.add_vertex((805, 1368))
    feet1.add_vertex((851, 1355))
    feet1.add_vertex((866, 1306))
    feet1.add_vertex((849, 1236))
    feet1.filled = True
    feet1.fill_color = "snow"
    feet1.color = "snow"
    window.add(feet1)

    feet2 = GPolygon()
    feet2.add_vertex((1027, 1102))
    feet2.add_vertex((1096, 1133))
    feet2.add_vertex((1142, 1117))
    feet2.add_vertex((1177, 1041))
    feet2.add_vertex((1166, 981))
    feet2.add_vertex((1114, 970))
    feet2.add_vertex((1053, 1002))
    feet2.filled = True
    feet2.fill_color = "snow"
    feet2.color = "snow"
    window.add(feet2)

    rock1 = GPolygon()
    rock1.add_vertex((685, 837))
    rock1.add_vertex((677, 878))
    rock1.add_vertex((721, 902))
    rock1.add_vertex((747, 895))
    rock1.add_vertex((764, 878))
    rock1.add_vertex((766, 850))
    rock1.add_vertex((741, 819))
    rock1.add_vertex((706, 821))
    rock1.filled = True
    rock1.fill_color = "black"
    rock1.color = "black"
    window.add(rock1)

    rock2 = GPolygon()
    rock2.add_vertex((763, 1014))
    rock2.add_vertex((764, 1065))
    rock2.add_vertex((784, 1087))
    rock2.add_vertex((819, 1072))
    rock2.add_vertex((835, 1065))
    rock2.add_vertex((857, 1021))
    rock2.add_vertex((839, 993))
    rock2.add_vertex((824, 988))
    rock2.add_vertex((794, 986))
    rock2.filled = True
    rock2.fill_color = "black"
    rock2.color = "black"
    window.add(rock2)

    rock3 = GPolygon()
    rock3.add_vertex((873, 1091))
    rock3.add_vertex((883, 1127))
    rock3.add_vertex((912, 1149))
    rock3.add_vertex((956, 1113))
    rock3.add_vertex((959, 1084))
    rock3.add_vertex((945, 1058))
    rock3.add_vertex((910, 1057))
    rock3.filled = True
    rock3.fill_color = "black"
    rock3.color = "black"
    window.add(rock3)

    leye1 = GOval(80, 80, x=786, y=337)
    leye1.filled = True
    leye1.fill_color = "snow"
    leye1.color = "black"
    window.add(leye1)

    reye1 = GOval(80, 80, x=860, y=377)
    reye1.filled = True
    reye1.fill_color = "snow"
    reye1.color = "black"
    window.add(reye1)

    leye2 = GOval(40, 40, x=806, y=364)
    leye2.filled = True
    leye2.fill_color = "black"
    leye2.color = "black"
    window.add(leye2)

    reye2 = GOval(40, 40, x=878, y=400)
    reye2.filled = True
    reye2.fill_color = "black"
    reye2.color = "black"
    window.add(reye2)

    leye3 = GOval(4, 4, x=837, y=381)
    leye3.filled = True
    leye3.fill_color = "snow"
    leye3.color = "snow"
    window.add(leye3)

    reye2 = GOval(4, 4, x=910, y=416)
    reye2.filled = True
    reye2.fill_color = "snow"
    reye2.color = "snow"
    window.add(reye2)

    mouth2 = GPolygon()
    mouth2.add_vertex((701, 445))
    mouth2.add_vertex((694, 463))
    mouth2.add_vertex((686, 525))
    mouth2.add_vertex((682, 597))
    mouth2.add_vertex((687, 655))
    mouth2.add_vertex((703, 700))
    mouth2.add_vertex((735, 723))
    mouth2.add_vertex((775, 728))
    mouth2.add_vertex((822, 699))
    mouth2.add_vertex((865, 656))
    mouth2.add_vertex((919, 603))
    mouth2.add_vertex((924, 562))
    mouth2.filled = True
    mouth2.fill_color = "darkgray"
    mouth2.color = "darkgray"
    window.add(mouth2)

    tooth = GPolygon()
    tooth.add_vertex((767, 522))
    tooth.add_vertex((757, 540))
    tooth.add_vertex((750, 582))
    tooth.add_vertex((763, 601))
    tooth.add_vertex((822, 630))
    tooth.add_vertex((857, 633))
    tooth.add_vertex((877, 602))
    tooth.add_vertex((882, 573))
    tooth.filled = True
    tooth.fill_color = "snow"
    tooth.color = "snow"
    window.add(tooth)

    mouth1 = GPolygon()
    mouth1.add_vertex((751, 405))
    mouth1.add_vertex((714, 397))
    mouth1.add_vertex((694, 405))
    mouth1.add_vertex((687, 427))
    mouth1.add_vertex((694, 459))
    mouth1.add_vertex((755, 538))
    mouth1.add_vertex((794, 571))
    mouth1.add_vertex((841, 593))
    mouth1.add_vertex((879, 600))
    mouth1.add_vertex((919, 602))
    mouth1.add_vertex((951, 599))
    mouth1.add_vertex((970, 575))
    mouth1.add_vertex((974, 548))
    mouth1.add_vertex((954, 518))
    mouth1.add_vertex((909, 486))
    mouth1.filled = True
    mouth1.fill_color = "white"
    mouth1.color = "white"
    window.add(mouth1)

    nose1 = GOval(95, 95, x=810, y=411)
    nose1.filled = True
    nose1.fill_color = "darkorange"
    nose1.color = "darkorange"
    window.add(nose1)

    nose2 = GOval(25, 20, x=870, y=470)
    nose2.filled = True
    nose2.fill_color = "orange"
    nose2.color = "orange"
    window.add(nose2)

    leyebrow = GPolygon()
    leyebrow.add_vertex((897, 296))
    leyebrow.add_vertex((843, 284))
    leyebrow.add_vertex((829, 289))
    leyebrow.add_vertex((802, 315))
    leyebrow.add_vertex((836, 296))
    leyebrow.add_vertex((893, 309))
    leyebrow.filled = True
    leyebrow.fill_color = "saddlebrown"
    leyebrow.color = "saddlebrown"
    window.add(leyebrow)

    reyebrow = GPolygon()
    reyebrow.add_vertex((919, 313))
    reyebrow.add_vertex((914, 325))
    reyebrow.add_vertex((943, 346))
    reyebrow.add_vertex((957, 362))
    reyebrow.add_vertex((962, 394))
    reyebrow.add_vertex((968, 362))
    reyebrow.add_vertex((963, 347))
    reyebrow.filled = True
    reyebrow.fill_color = "saddlebrown"
    reyebrow.color = "saddlebrown"
    window.add(reyebrow)

    rarm = GPolygon()
    rarm.add_vertex((789, 801))
    rarm.add_vertex((798, 796))
    rarm.add_vertex((858, 780))
    rarm.add_vertex((873, 762))
    rarm.add_vertex((907, 747))
    rarm.add_vertex((934, 727))
    rarm.add_vertex((973, 707))
    rarm.add_vertex((991, 687))
    rarm.add_vertex((1016, 670))
    rarm.add_vertex((1009, 645))
    rarm.add_vertex((1013, 635))
    rarm.add_vertex((1026, 657))
    rarm.add_vertex((1045, 628))
    rarm.add_vertex((1060, 576))
    rarm.add_vertex((1072, 584))
    rarm.add_vertex((1064, 627))
    rarm.add_vertex((1102, 605))
    rarm.add_vertex((1111, 617))
    rarm.add_vertex((1075, 637))
    rarm.add_vertex((1115, 642))
    rarm.add_vertex((1113, 653))
    rarm.add_vertex((1070, 656))
    rarm.add_vertex((1033, 673))
    rarm.add_vertex((1016, 697))
    rarm.add_vertex((977, 717))
    rarm.add_vertex((951, 740))
    rarm.add_vertex((926, 761))
    rarm.add_vertex((896, 771))
    rarm.add_vertex((866, 797))
    rarm.add_vertex((844, 804))
    rarm.add_vertex((826, 824))
    rarm.add_vertex((804, 833))
    rarm.filled = True
    rarm.fill_color = "saddlebrown"
    rarm.color = "saddlebrown"
    window.add(rarm)

    label = GLabel('Olaf !')
    label.color = 'snow'
    label.font = 'Verdana-90-italitic'
    window.add(label, 50, 1400)


if __name__ == '__main__':
    main()
